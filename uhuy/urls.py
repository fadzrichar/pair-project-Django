from django.contrib import admin
from django.urls import path
from . import views

app_name = 'uhuy'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('profile',views.profile, name = 'profile'),
    path('details/<int:place_id>',views.details, name = 'details'),
    path('toplist',views.toplist, name = 'toplist')    
]