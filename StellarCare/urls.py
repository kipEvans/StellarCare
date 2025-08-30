
from django.contrib import admin
from django.urls import path, include
from StellarCareapp import views

urlpatterns = [
    path('', include('StellarCareapp.urls')),
]
