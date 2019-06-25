from django.shortcuts import render,redirect
from django.http import*
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login as dj_login
from autho.form import userformA
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	return render(request, 'index.html', {})




#registration
def reg(request):
	if request.method == "POST":
		formA = userformA(request.POST)
		if formA.is_valid():
			username = formA.cleaned_data['username']
			email = formA.cleaned_data['email']
			first_name = formA.cleaned_data['first_name']
			password = formA.cleaned_data['password']
			User.objects.create_user(username=username, email=email, first_name=first_name, password=password)
			return redirect('/auth/login/')
	
	else:
		formA = userformA()
	return render(request, 'reg.html', {'formA':formA})	



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                dj_login(request,user)
                return render(request, 'success.html')
                #return HttpResponseRedirect(reverse('success'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


		

@login_required(login_url="/login/")
def success(request):
	context = {}
	context['user'] = request.user
	return render(request, "success.html", context)




    
def logout(request):
	django_logout(request)
	msg = messages.success(request,'Successfully Logout')
	return redirect('/')