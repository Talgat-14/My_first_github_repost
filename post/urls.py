from django.urls import path
from . import views 
urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('contact/', views.contactPage, name='contact'),
    path('jandarbek/', views.jandarbek, name='jandarbek'),
    path('talgat/', views.talgat, name='talgat'),
    path('sharyar/', views.sharyar, name='sharyar'),
]