from django.contrib import admin
from kinopoisk.models import * 

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
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
@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
      list_display=(
        'name',
      )

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
      list_display=(
        'author',
        'movie',
        'likes',
  
     
      )