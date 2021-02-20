from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


urlpatterns = [
    path("", views.index, name="index"),
    path("restaurantes", views.restaurant, name="restaurants"),
    path("abarrotes", views.store, name="store"),
    path("restaurantes/<url>", views.restPage, name="restaurant_page"),
    path("abarrote/<url>", views.storePage, name="store_page"),
    path("salud", views.salud, name="salud"),
    path("salud/instituciones/<url>", views.saludPage, name="salud_page"),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)