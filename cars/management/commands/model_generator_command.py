from django.core.management import BaseCommand
import pandas as pd
from gensim.models import Word2Vec
import pickle

from cars.models import Car


def save_binary(file_path, car_vectors):
    with open(file_path, 'wb') as file:
        pickle.dump(car_vectors, file)


def get_cars_from_db():
    cars_queryset = Car.objects.all()
    df_cars = pd.DataFrame.from_records(cars_queryset.values())
    return df_cars


class Command(BaseCommand):
    help = 'Generates Word Embeddings'

    def handle(self, *args, **options):
        self.stdout.write('Generating model and vector representations...')

        # Fetch data from the Car model
        df_cars = get_cars_from_db()

        # Convert MSRP to buckets
        bins = [0, 20000, 40000, 60000, 80000, float('inf')]
        labels = ['Low', 'Mid-Low', 'Mid-Range', 'High-Range', 'Luxury']
        df_cars['msrp_bucket'] = pd.cut(df_cars['msrp'], bins=bins, labels=labels, include_lowest=True)

        # Convert categorical columns to strings
        df_cars['make'] = df_cars['make'].astype(str)
        df_cars['model'] = df_cars['model'].astype(str)
        df_cars['year'] = df_cars['year'].astype(str)
        df_cars['msrp_bucket'] = df_cars['msrp_bucket'].astype(str)

        # Combine all textual data into a single column for embedding
        df_cars['text_data'] = df_cars['make'] + ' ' + df_cars['model'] + ' ' + df_cars['year'] + ' ' + df_cars[
            'msrp_bucket'] + ' ' + df_cars['market_category']

        # Drop missing values in the 'text_data' column
        df_cars = df_cars.dropna(subset=['text_data'])

        # Train Word2Vec model
        model = Word2Vec(sentences=df_cars['text_data'].apply(lambda x: x.split()), vector_size=50, window=5,
                         min_count=1, workers=4)

        # Save model using pickle
        save_binary('cars/word_embedding_models/car_embeddings.pkl', model)

        # Calculate vector representations for all cars
        car_vectors = [sum(model.wv[word] for word in text.split()) for text in df_cars['text_data']]

        # Save the car vectors to a binary file
        save_binary('cars/word_embedding_models/car_vectors.pkl', car_vectors)
