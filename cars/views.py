from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def cars_list(request):
    """
    List all car recommendations
    """
    if request.method == 'GET':

        return JsonResponse("{}", safe=False, status=200)