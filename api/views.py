from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Ratings
from .serializers import MovieSerializer, RatingsSerializer

# Create your views here.
class MovieViewset(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class= MovieSerializer

class RatingsViewset(viewsets.ModelViewSet):
    queryset=Ratings.objects.all()
    serializer_class= RatingsSerializer
