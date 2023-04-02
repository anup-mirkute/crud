from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DetailForm
from .models import Detail


# Create your views here.
def index(request):
    details = Detail.objects.all()
    form = DetailForm

    context = {
        'details' : details,
        'form' : form,
    }
    return render(request, 'index.html', context)

def addDetails(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']

        add_detail = Detail(name=name, email=email, address=address)
        add_detail.save()

    return redirect('index')

def update(request, id):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']

        detail = Detail.objects.get(id=id)
        detail.name = name
        detail.email = email
        detail.address = address
        detail.save()
    return redirect('index')

def delete(request, id):
    detail = Detail.objects.get(id=id)
    detail.delete()
    return redirect('index')