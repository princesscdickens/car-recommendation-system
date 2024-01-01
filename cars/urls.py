from django.urls import path

from cars.views import cars_list

urlpatterns = [
    path('api/v1/cars/', cars_list)
]