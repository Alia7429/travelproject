from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import People


# Create your views here.
def new(request):
    obj = Place.objects.all()
    a = People.objects.all()
    return render(request, "index.html", {'result': obj, 'next': a})
