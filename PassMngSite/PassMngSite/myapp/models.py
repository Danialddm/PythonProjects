from django.contrib.auth.models import User
from django.db import models

# Create your models here. class=entity, property=coloumn
class Publisher (models.Model): #har class yek id ya p.k darad
    name = models.CharField(max_length=30) #CharField=varchar
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __str__(self): #display text of name b jaye publisher.object
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)#ejbari va ehtiari kardane field

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author) #chand b chand
    publisher = models.ForeignKey(Publisher,on_delete=models.DO_NOTHING)
    publication_date = models.DateField(blank=True,null=True)

class PassEntry(models.Model):
    pass_word = models.CharField(max_length=32)#dar class form limit password set mishavad.
    user_name = models.CharField(max_length=100)
    service_name = models.CharField(max_length=50)
    desc_comm = models.CharField(max_length=500, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)