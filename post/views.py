from django.shortcuts import render
from django.http import HttpResponse 

def homePage(request):
	return render(request, 'base.html')
def aboutPage(request):
	return render(request, 'post/about.html')
def contactPage(request):
	return render(request, 'post/contact.html')
def jandarbek(request):
	return render(request, 'post/jandarbek.html')
def talgat(request):
	return render(request, 'post/talgat.html')
def sharyar(request):
	return render(request, 'post/sharyar.html')
	
