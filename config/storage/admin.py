from django.contrib import admin
from .models import * 

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display=(
        'poster',
        'title',
    )
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
        list_display=(
            'name',
            'id',
   )
@admin.register(FilmPerson)
class FilmPersonAdmin(admin.ModelAdmin):
      list_display=(
        'actor',
        'composer',
        'director',
        'screenwriter',
        'producer',
      )

@admin.register(FilmReview)
class FilmReviewAdmin(admin.ModelAdmin):
      list_display=(
        'author',
        'film',
        'likes',
        'dislikes',  
        'created_at',  
      )