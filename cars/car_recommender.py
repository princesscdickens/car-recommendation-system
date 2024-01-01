import pickle
from sklearn.metrics.pairwise import cosine_similarity
from cars.models import Car


def load_binary(file_path):
    with open(file_path, 'rb') as file:
        file_content = pickle.load(file)
    return file_content

def get_cars_queryset_from_db_by_ids(ids):
    return Car.objects.filter(id__in=ids)


def get_car_recommendations(car_features, number_of_recommendations):
    # Load model saved location
    model = load_binary('cars/word_embedding_models/car_embeddings.pkl')

    # Get the vector representation of the input car features
    input_vector = sum([model.wv[word] for word in car_features.split()])

    # Load pre calculated vector
    car_vector = load_binary('cars/word_embedding_models/car_vectors.pkl')

    # Calculate cosine similarity between input car and all other cars
    similarities = cosine_similarity([input_vector], car_vector)[0]

    # Get indices of top n similar cars
    indices = similarities.argsort()[-number_of_recommendations - 1:-1][::-1]

    # Display recommended cars
    return get_cars_queryset_from_db_by_ids(indices)

