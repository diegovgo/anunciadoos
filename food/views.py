from django.shortcuts import render, redirect
from .models import District, Restaurant, Dishes, Category, Saludinst
from django.http import HttpResponseRedirect, HttpResponse
#from .forms import NoteForm, CustomUserForm, CreatePostForm, FileForm, MyUserForm
#from rest_framework import viewsets
#from .serializers import CourseSerializer, FileSerializer, NoteSerializer, MyUserSerializer, UniversitySerializer, CareerSerializer
#from django.contrib.auth.decorators import login_required, permission_required
#from django.contrib.auth import authenticate, login
#from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    categorys = Category.objects.all()
    data = {
        'categorys': categorys
    }
    return render(request, 'food/index.html', data)


def restaurant(request):
    restaurants = Restaurant.objects.all()
    data = {
        'restaurants': restaurants,
    }
    return render(request, 'food/restaurants.html', data)


def restPage(request, id):
    restaurant = Restaurant.objects.get(id=id)
    dishes = Dishes.objects.filter(restaurant=restaurant)
    data = {
        'restaurant': restaurant,
        'dishes': dishes,
    }
    print(dishes)
    return render(request, 'food/restaurant_page.html', data)

def salud(request):
    instituciones = Saludinst.objects.all()
    data = {
        'instituciones' : instituciones
    }
    print(instituciones)
    return render(request, 'food/salud.html', data)

def saludPage(request, url):
    institucion = Saludinst.objects.get(url=url)
    data = {
        'institucion': institucion,
    }

    return render(request, 'food/salud_page.html', data)
