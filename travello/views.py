from django.shortcuts import render
from .models import Destination
###from http import request
# Create your views here.
def index(request):
    
    dests=Destination.objects.all()

    return render(request,'index.html' , {'dests': dests})