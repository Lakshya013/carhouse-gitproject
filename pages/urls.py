from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about,name='about'),
    path('cars',views.car,name='car'),
    path('services', views.services,name='services'),
    path('contact', views.contact, name='contact'),
]
