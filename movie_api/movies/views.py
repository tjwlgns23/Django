from .serializers import MovieSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer