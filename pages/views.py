from django.shortcuts import render


# Create your views here.

# 4th step since we create views.home we are making the functoin inside the views

def home(request):
    return render(request, 'pages/home.html')  # hence we will create a new folder for pages/home


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')


def about(request):
    return render(request, 'pages/about.html')


def car(request):
    return render(request, 'pages/car.html')
