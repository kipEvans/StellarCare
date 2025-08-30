
from django.contrib import admin
from django.urls import path

from StellarCareapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('error/', views.error,name='error'),
    path('about/', views.about,name='about'),
    path('appointment/', views.appointment,name='appointment'),
    path('contact/', views.contact,name='contact'),
    path('department-details/', views.department,name='department-details'),
    path('departments/', views.departments,name='departments'),
    path('doctors/', views.doctors,name='doctors'),
    path('faq/', views.faq,name='faq'),
    path('gallery/', views.gallery,name='gallery'),
    path('home/', views.index,name='index'),
    path('', views.index,name='home'),
    path('privacy/', views.privacy,name='privacy'),
    path('service-details/', views.service,name='service-details'),
    path('services/', views.services,name='services'),
    path('starter/', views.starter,name='starter'),
    path('terms/', views.terms,name='terms'),
    path('testimonials/', views.testimonials,name='testimonials'),
]
