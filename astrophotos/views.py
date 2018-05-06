from django.shortcuts import render
from django.http  import HttpResponse,Http404
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
     if 'category' in request.GET and request.GET['category']:
           search_category = request.GET.get('category')
           searched_categories = Image.search_by_category(search_category)
           message = f"{search_category}"

           return render(request, 'search.html', {"message":message, "categories":searched_categories})

     else:
           message = "You haven't searched for any term"

           return render(request, 'search.html',{"message":message})
     
