from django.db import models
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)
        
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
