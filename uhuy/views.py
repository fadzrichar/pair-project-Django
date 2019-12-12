from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.

def home(request):
    fields = {"destinations": Destination.objects.all()[:4:-1]}
    return render(request, 'uhuy/home.html', fields)

def details(request, place_id):
    destinations = Destination.object.get(pk=place_id)
    return render(request, 'uhuy/details.html', {"destination" : destinations})

def toplist(request):
    return render(request, 'uhuy/toplist.html', {})

def profile(request):
    return render(request, 'uhuy/profile.html', {})