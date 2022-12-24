from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
	return render(request, 'home.html')

def book_time(request):
	return render(request, 'form.html',{
		'book_time':book_time
		})

def service(request):
	return render(request, 'service.html',{
		'service':service
		})
def product(request):
	return render(request, 'product.html')

def about(request):
	return render(request, 'about.html')

def homelist(request):
	persons = Person.objects.all()
	return render(request, 'view.html',{
		'persons':persons
		})