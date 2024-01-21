from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from .models import Movie, Ratings
from .serializers import MovieSerializer, RatingsSerializer

# Create your views here.
class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    @action(detail=True, methods=["POST"])
    def rate_movie(self, request, pk=None):
        
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            # user = User.objects.get(id=1)
            user = request.user
            
            try:
                rating = Ratings.objects.get(user=user.id, movie=movie)
                rating.stars = stars
                rating.save()
                serializer = RatingsSerializer(rating, many=False)
                response = {'message':'Updated', 'result:':serializer.data }
            except:
                rating = Ratings.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingsSerializer(rating, many=False)
                response = {'message':'Created', 'result:':serializer.data}
            
        else:
            response = {'pk': 'Need stars in request'}
            
        return Response(response, status=status.HTTP_200_OK)

        

class RatingsViewset(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
