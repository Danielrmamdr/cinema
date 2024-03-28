from django.shortcuts import render

# Create your views here.
def actor_detail(request):
    return render(request, 'storage/actor_detail.html')

def composer_detail(request):
    return render(request, 'storage/composer_detail.html')

def director_detail(request):
    return render(request, 'storage/director_detail.html')

def genre_detail(request):
    return render(request, 'storage/genre_detail.html')

def movie_detail(request):
    return render(request, 'storage/movie_detail.html')

def producer_detail(request):
    return render(request, 'storage/producer_detail.html')

def screenwriter_detail(request):
    return render(request, 'storage/screenwriter_detail.html')

def storage(request):
    return render(request, 'storage/storage.html')

def movie_persons(request):
    return render(request, 'storage/movie_persons.html')