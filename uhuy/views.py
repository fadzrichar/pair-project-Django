from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from .form import *
from django.urls import reverse
from django.db.models import Q
# from django.views.generic import ListView
# Create your views here.

def home(request):
    destinations = Destination.objects.all().order_by("-dest_rating")
    total = len(destinations)
    fields = {"destinations": destinations[:4:], "user": User.objects.get(pk=1), "total":total}
    return render(request, 'uhuy/home.html', fields)

def details(request, place_id):
    destinations = Destination.objects.get(pk=place_id)
    profile = User.objects.get(pk=1)
    return render(request, 'uhuy/details.html', {"destination" : destinations, "user": profile})

def toplist(request):
    destinations = Destination.objects.all().order_by("-dest_rating")
    fields = {"destinations": destinations, "user": User.objects.get(pk=1)}
    return render(request, 'uhuy/toplist.html', fields)

def search_result(request):
    q = request.POST["keyword"]
    destinations = Destination.objects.filter(Q(dest_name__icontains=q) | Q(dest_country__icontains=q))
    fields = {"destinations": destinations, "user": User.objects.get(pk=1), "keyword": q}
    return render(request, 'uhuy/search_result.html', fields)

def profile(request):
    fields = {"user": User.objects.get(pk=1)}
    return render(request, 'uhuy/profile.html', fields)

def change_profile_pic(request):
#     user = User.objects.get(pk=1)
#     user.picture = request.POST['']
#     user.save()
    # if request.POST:
    #     user = UserForm(request.POST, request.FILES)
    #     if user.is_valid():
    #         user.save()
    #     else:
    #         print(user.errors)
    #     return HttpResponseRedirect(reverse('uhuy:home'))

    # fields = {"user": User.objects.get(pk=1), "form":UserForm}
    return render(request, 'uhuy/profile.html', fields)
