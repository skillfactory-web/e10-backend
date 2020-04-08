from django.db import models


class Drink(models.Model):
    name = models.CharField('название', max_length=128)
    description = models.TextField('описание', null=True)
    rating = models.IntegerField()
