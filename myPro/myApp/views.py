from django.shortcuts import render
from .models import Cocktail
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "myApp/Home.html")

def page2(request):
    return render(request, "myApp/Page2.html")

def page3(request):
    return render(request, "myApp/Page3.html")

def page4(request):
    return render(request, "myApp/Page4.html")

def page5(request):
    return render(request, "myApp/Page5.html")

def cocktails(request):
    allDrink = Cocktail.objects.all()
    return render(request, 'myApp/PageForCocktails.html',{'allDrink': allDrink})
