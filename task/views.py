from django.shortcuts import render
from django.http import HttpResponse
from .forms import Detail, Address
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    details = User.objects.all()
    userform = Detail
    addressform = Address
    context = {
        'details': details,
        'userform':userform,
        'addressform':addressform,
    }
    return render(request, 'index.html', context)

def addDetails(request):
    
    return render(request, 'index.html')