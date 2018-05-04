from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home(request):
    
    return render(request,"home.html")
def planets(request):
    
    return render(request,"category/planets.html")    
def stars(request):
    
    return render(request,"category/stars.html")
def comets(request):
    
    return render(request,"category/comets.html")
def asteroids(request):
    
    return render(request,"category/asteroids.html")
def auroras(request):
    
    return render(request, "category/auroras.html")