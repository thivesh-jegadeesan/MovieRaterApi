from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.\
    
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=360)
    
    def no_of_ratings(self):
        ratings= Ratings.objects.filter(movie=self)
        return len(ratings)
    
    def average_rating(self):
        sum=0
        ratings= Ratings.objects.filter(movie=self)

        for rating in ratings:
            sum += rating.stars
            
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0
    
class Ratings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    class meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)