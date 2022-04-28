from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
	return render(request, 'landingpagedesign/index.html')

