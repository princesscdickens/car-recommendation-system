import pandas as pd
from django.core.management import BaseCommand
from cars.car_recommender import get_car_recommendations


class Command(BaseCommand):
    help = 'Generates Recommendations'

    def add_arguments(self, parser):
        parser.add_argument('Make', type=str, help='The make of the car')
        parser.add_argument('Model', type=str, help='The model of the car')
        parser.add_argument('Year', type=str, help='The year of the car')
        parser.add_argument('MSRP', type=str, help='The manufacturer suggested retail price of the car')

    def handle(self, *args, **options):
        self.stdout.write('Getting Recommendations')
        make = options['Make']
        model = options['Model']
        year = options['Year']
        msrp = options['MSRP']
        # Convert categorical columns to strings

        # Combine all textual data into a single column for embedding
        input_car_features = ' '.join([make, model, year, msrp])

        # Load model saved location
        cars = get_car_recommendations(input_car_features, 5)
        df_cars = pd.DataFrame.from_records(cars.values())
        print(df_cars)
