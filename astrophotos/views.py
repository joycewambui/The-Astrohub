from django.shortcuts import render
from django.http  import Http404
from .models import Image,Category,Location


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


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get('image') 
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"images": searched_images})
        
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})