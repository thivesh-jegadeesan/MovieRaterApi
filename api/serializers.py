from rest_framework import serializers
from .models import Movie, Ratings

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'no_of_ratings', 'average_rating')
        
class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('id', 'stars', 'user', 'movie')