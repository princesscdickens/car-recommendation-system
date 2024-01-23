from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from cars.car_recommender import get_car_recommendations
from cars.serializers import CarSerializer


@csrf_exempt
def cars_list(request):
    """
    List all cars recommendations.
    """
    if request.method == 'GET':
        # Extracting GET parameters
        make = request.GET.get('make')
        model = request.GET.get('model')
        year = request.GET.get('year')
        msrp = request.GET.get('msrp')
        number_of_recommendations = int(request.GET.get('number_of_recommendations')) if request.GET.get(
            'number_of_recommendations') else 5

        # Check if any parameter is missing
        if any(param is None for param in [make, model, year, msrp]):
            return JsonResponse({'error': 'Missing one or more parameters: make, model, year, msrp'}, status=400)

        # Join them
        input_car_features = ' '.join([make, model, year, msrp])

        cars = get_car_recommendations(input_car_features, number_of_recommendations)
        serializer = CarSerializer(cars, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)