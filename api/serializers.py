from rest_framework import serializers
from .models import Movie, Ratings

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description')
        
class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('id', 'stars', 'user', 'movie')