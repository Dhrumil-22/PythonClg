from django.shortcuts import render
from .models import Movie
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    template_data = {'title':'Movies',
                     'movies':movies}
    return render(request, 'index.html',
                  {'template_data':template_data})