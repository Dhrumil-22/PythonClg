from django.shortcuts import render
from .models import Movie,Review
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    template_data = {'title':'Movies',
                     'movies':movies}
    return render(request, 'index.html',
                  {'template_data':template_data})

def show(request,id):
    movie = Movie.objects.get(id=id)
    name = movie.name
    template_data = {'title':name,'movie':movie}
    
    return render(request,'show.html',{'template_data':template_data})

def create_review(request,id):
    if request.method == "POST" and request.POST("comment") != '':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.commnet  = request.POST['comment']
        review.movie = movie
        review.user = request.user
        review.save()
    
        
