from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
	response = "This is a placeholder to later display all the list of blogs!"
	return HttpResponse (response)

def new(request):
	response = "This is a placeholder to display a new form to create a new blog."
	return HttpResponse(response)

def create(request):
	if request.method == "POST":
		print("*"*50)
		print(requst.POST)
		print(request.POST['name'])
		print(request.POST['desc'])
		request.session['name'] = "test"
		print("*"*50)
		return redirect("/")
	else:
		return redirect("/")

def show(request, number):
	response = "This is a placeholder to display blog "+number+ "."
	return HttpResponse(response)

def edit(request, number):
	response = "This is a placeholder to edit blog " +number+"."
	return HttpResponse(response)

def destroy(request, number):
	return redirect('/')