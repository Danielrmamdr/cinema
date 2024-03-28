from django.db import models
from core.models import User

# Create your models here.
class FilmPerson(models.Model):
    class RoleType(models.TextChoices):
        PRODUCER = "producer", "Producer"
        ACTOR = "actor", "Actor"
        DIRECTOR = "director", "Director"
        COMPOSER = "composer", "Composer"
        SCREENWRITER = "screenwriter", "Screenwriter"
    role = models.CharField(
        max_length=255,
        choices = RoleType.choices,
        blank=True,
        null=True
        )
    
    name = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to="films/images/person/"
    )
    biography = models.TextField()
    birthday = models.DateField()

class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Film(models.Model):       
    title = models.CharField(max_length=255)
    poster = models.ImageField(
        upload_to="films/images/posters/"
    )
    producer = models.ManyToManyField(FilmPerson, related_name="profuced_films")
    actor = models.ManyToManyField(FilmPerson, related_name="acted_films")
    director = models.ManyToManyField(FilmPerson, related_name="directed_films")
    composer = models.ManyToManyField(FilmPerson, related_name="composed_films")
    screenwriter = models.ManyToManyField(FilmPerson, related_name="wrote_films")
    genres = models.ManyToManyField(Genre, related_name="movies")
    year = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=255, default="USA")
    description = models.TextField(null=True)
    budget = models.PositiveBigIntegerField(default=0)
    duration = models.SmallIntegerField(default=23)
    agelimit = models.SmallIntegerField(default=0)
    trailer =  models.CharField(max_length=500, null=True)
    
class FilmReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="reviews")
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)