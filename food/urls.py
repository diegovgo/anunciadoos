from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


urlpatterns = [
    path("", views.index, name="index"),
    path("comida", views.restaurant, name="comida"),
    path("restaurante/<id>", views.restPage, name="restaurant_page"),
    path("salud", views.salud, name="salud"),
    path("salud/instituciones/<url>", views.saludPage, name="salud_page"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)