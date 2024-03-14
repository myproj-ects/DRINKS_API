from django.db import models

# Django model for representing drinks
class Drink(models.Model):
    # Define fields for the Drink model
    name = models.CharField(max_length=200)  # Field for storing the name of the drink
    description = models.CharField(max_length=500)  # Field for storing the description of the drink

    # Method to return a string representation of the Drink object
    def __str__(self):
        return self.name + ' ' + self.description
    