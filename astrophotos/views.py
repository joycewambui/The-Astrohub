from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image


# Create your views here.
def home(request):
    
    return render(request,"home.html")

def images(request):
    
    images =Image.objects.all()    
    
    return render(request,"images.html", {"images": images})
