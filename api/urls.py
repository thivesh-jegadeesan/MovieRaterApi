from django.urls import path
from rest_framework import routers
from django.urls import include
from .views import MovieViewset, RatingsViewset

routers = routers.DefaultRouter()
routers.register('movies', MovieViewset)
routers.register('ratings', RatingsViewset)


urlpatterns = [
    path('', include(routers.urls))
]