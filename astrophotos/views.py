from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image


# Create your views here.
def home(request):
    
    images =Image.objects.all()    
    
    return render(request,"home.html", {"images": images})

def images(request, image_id):
     try:
           images = Image.objects.get(id = image_id)
     except Image.DoesNotExist:
           raise Http404()

     return render(request,"images.html", {"images":images})
     
