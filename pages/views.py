from django.shortcuts import render

# Create your views here.

# 4th step since we create views.home we are making the functoin inside the views
from pages.models import Team


def home(request):
    teams = Team.objects.all()
    # data = {
    #     'teams': teams,
    # }
    return render(request, 'pages/home.html', {'teams': teams})  # hence we will create a new folder for pages/home


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def car(request):
    return render(request, 'pages/car.html')
