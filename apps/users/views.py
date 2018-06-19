from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
def register(request):
	response = "This is a placeholder for users to create a new user record!"
	return HttpResponse (response)

def login(request):
	response = "This is a placeholder for users to creat a new user record!"
	return HttpResponse(response)

def users(request):
	response = "This is a placeholder to later display a list of all the users."