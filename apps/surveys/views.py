from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
def surveys(request):
	response = "This is a placeholder to later display surveys created!"
	return HttpResponse (response)

def new(request):
	response = "This is a placeholder for users to add a new survey."
	return HttpResponse(response)