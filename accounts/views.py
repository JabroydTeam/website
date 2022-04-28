from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.



def signup(request):
	if request.method == 'POST':
		email = request.POST['email']
		username = request.POST['username']
		#phone = request.POST['phone']
		password = request.POST['password']
		repassword = request.POST['repassword']
		user = User.objects.create_user(username=username, email=email, password=password)
		user.save()
		print('user created')

		#messages.success(request,"Your account has been successfully created")
		return redirect('/')


	else:
		return render(request, 'landingpagedesign/register.html')






def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)


		if user is not None:
			auth.login(request, user)
			#name = user.name
			return render(request, 'dashboarddesign/index.html')

		else:
			#messages.error(request, "Bad Credentials")	
			return render(request, 'landingpagedesign/abd.html')

	else :
		return render(request, 'landingpagedesign/login.html')	



def signout(request):
	pass