from django.db import models

# Create your models here.
class Car(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    engine_fuel_type = models.CharField(max_length=255,null=True, blank=True)
    engine_hp = models.IntegerField(null=True, blank=True)
    engine_cylinders = models.IntegerField(null=True, blank=True)
    transmission_type = models.CharField(max_length=255)
    driven_wheels = models.CharField(max_length=255)
    number_of_doors = models.IntegerField(null=True, blank=True)
    market_category = models.CharField(max_length=255)
    vehicle_size = models.CharField(max_length=255)
    vehicle_style = models.CharField(max_length=255)
    highway_mpg = models.IntegerField()
    city_mpg = models.IntegerField()
    popularity = models.IntegerField()
    msrp = models.IntegerField()

    class Meta:
        ordering = ['created']