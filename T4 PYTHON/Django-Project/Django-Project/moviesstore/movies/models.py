from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_img/')
    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    commnet = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE) 
    user = models.ForeignKey(User, on_delete= models.CASCADE) 




