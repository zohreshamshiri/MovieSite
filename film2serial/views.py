from django.shortcuts import render, HttpResponse,redirect
from .models import Movie
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.views import generic
# Create your views here.

def homepage(request):
    pass
def show_movies(request):
    all_movies= Movie.objects.all()
    #return HttpResponse(all_movies)
    return render(request,'index.html',{'movies':all_movies})

def search(request):
    query = request.GET.get('query', '')
    if query:
        movies = Movie.objects.filter(original_title__icontains=query)
    else:        movies = Movie.objects.all()

    return render(request, 'list.html', {'movies': movies})

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(request, username=username , password=password)
        if user is not None:
            login(request,user,)
            messages.success(request,("با موفقیت وارد شدید"))
            return redirect("home")
        else:
            messages.success(request, ("مشکل در روند ورود"))
            return redirect("login")
    else:
        return render(request, 'login.html' )



def logout_user(request):
    logout(request)
    messages.success(request, ("با موفقیت خارج شدید"))
    return redirect("home")


class MovieListView(generic.ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'list.html'


def search(request):
    query = request.GET.get('query', '')
    if query:
        movies = Movie.objects.filter(original_title__icontains=query)
    else:
        movies = Movie.objects.all()

    return render(request, 'list.html', {'movies': movies})



