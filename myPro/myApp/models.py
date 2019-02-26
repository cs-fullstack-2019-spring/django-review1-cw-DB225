from django.db import models

# Create your models here.
class Cocktail(models.Model):
    name = models.CharField(max_length=200)
    alcohol_percentage = models.IntegerField()
    serving_glass = models.CharField(max_length=200)

    def __str__(self):
        return self.name
