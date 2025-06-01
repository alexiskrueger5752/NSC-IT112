from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 100, default='')
    genre = models.CharField(max_length = 100, default='')
    year = models.IntegerField(default=2025)

    def __str__(self):
        return self.title