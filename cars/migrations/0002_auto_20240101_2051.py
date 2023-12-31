# Generated by Django 5.0 on 2024-01-01 20:51

from django.db import migrations
import csv

def load_data(apps, schema_editor):
    Car = apps.get_model('cars', 'Car')

    # Open and read the CSV file
    with open('/app/cars/migrations/car_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Car.objects.create(
                make=row['Make'],
                model=row['Model'],
                year=int(row['Year']),
                engine_fuel_type=row['Engine Fuel Type'],
                engine_hp=int(row['Engine HP']) if row['Engine HP'] else None,
                engine_cylinders=int(row['Engine Cylinders']) if row['Engine Cylinders'] else None,
                transmission_type=row['Transmission Type'],
                driven_wheels=row['Driven_Wheels'],
                number_of_doors=int(row['Number of Doors']) if row['Number of Doors'] else None,
                market_category=row['Market Category'],
                vehicle_size=row['Vehicle Size'],
                vehicle_style=row['Vehicle Style'],
                highway_mpg=int(row['highway MPG']),
                city_mpg=int(row['city mpg']),
                popularity=int(row['Popularity']),
                msrp=int(row['MSRP'])
            )


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
