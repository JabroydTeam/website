from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
	return render(request, 'landingpagedesign/index.html')


def signup(request):
	if request.method == "POST":
		email = request.POST['email']
		phone = request.POST['phone']
		password = request.POST['password']
		repassword = request.POST['repassword']
		
		myuser = User.objects.create_user(email, password)
		myuser.phone = phone

		myuser.save()

		messages.success(request,"Your account has been successfully created")

		return redirect('../signin')


	return render(request, 'landingpagedesign/register.html')






def signin(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']

		user = authenticate(email=email, password=password)

		if user is not None:
			login(request, user)
			name = user.name
			return render(request, "templates/dashboarddesign/index.html", {'name':name})

		else:
			messages.error(request, "Bad Credentials")	
			return redirect('../dashboard/')


	return render(request, 'landingpagedesign/login.html')	



def signout(request):
	pass