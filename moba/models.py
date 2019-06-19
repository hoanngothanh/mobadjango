from django.db import models


# Create your models here.
class HeroList(models.Model):
    hero_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=200)
    data_stars = models.CharField(max_length=100)

    class Meta:
        ordering = (('name'),)
