from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home(request):
    
    return render(request,"home.html")

def Imagestock(request):
    
    return render(request,"imagestock.html")
