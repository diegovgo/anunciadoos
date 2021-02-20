from django.shortcuts import render, redirect
from .models import District, Restaurant, Dishes, Category, Saludinst, TypeOf, Article, Storesubcategory, Store
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
    class Restaurantin:
        def __init__(self, name, url, categorys, logo, description, deliveryprice):
            self.name = name
            self.url = url
            self.categorys = categorys
            self.logo = logo
            self.description = description
            self.deliveryprice = deliveryprice

    restaurants_lists = list()

    for restaurant in restaurants:
        restaurants_lists.append(Restaurantin(restaurant.name, restaurant.url, restaurant.typeof.all() , restaurant.logo.url, "blablablab", "3.99"))

    bravewings = restaurants_lists[2]
    diegos = bravewings.categorys
    for diego in diegos:
        print(diego.name)


    data = {
        'restaurants': restaurants_lists
    }
    return render(request, 'food/restaurants.html', data)

def store(request):
    stores = Store.objects.all()
    print(store)
    data = {
        'stores': stores,
    }
    return render(request, 'food/store.html', data)

def restPage(request, url):
    restaurant = Restaurant.objects.get(url=url)
    try:
        my_districts = restaurant.district.all()
    except:
        my_districts = restaurant.district.filter()[0]
        print(my_districts)
    else:
        print("Nothing went wrong")
    typeofs = restaurant.typeof.order_by('order')
    ##dishes = Dishes.objects.filter(typeof)
    dishes = []
    elements = ""
    for typeof in typeofs:
        dishes.extend(typeof.dishes.all())
        elements = elements + " - " + typeof.name

    districts = ""
    for my_district in my_districts:
        districts = districts + " - " + my_district.name


    print(districts)
    data = {
        'restaurant': restaurant,
        'dishes': dishes,
        'typeofs': typeofs,
        'elements': elements,
        'districts': districts,
        
    }
    print(typeofs)
    return render(request, 'food/restaurant_page.html', data)

def storePage(request, url):
    store = Store.objects.get(url=url)
    try:
        my_districts = store.district.all()
    except:
        my_districts = store.district.filter()[0]
        print(my_districts)
    else:
        print("Nothing went wrong")
    storesubcategorys = store.storesubcategory.order_by('order')
   
    ##dishes = Dishes.objects.filter(typeof)
    articles = []
    elements = ""
    for storesubcategory in storesubcategorys:
        articles.extend(storesubcategory.article.all())
        elements = elements + " - " + storesubcategory.name

    districts = ""
    for my_district in my_districts:
        districts = districts + " - " + my_district.name


    print(districts)
    data = {
        'store': store,
        'articles': articles,
        'storesubcategorys': storesubcategorys,
        'elements': elements,
        'districts': districts,
        
    }
    
    return render(request, 'food/store_page.html', data)

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
