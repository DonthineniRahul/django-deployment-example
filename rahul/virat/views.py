from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from virat import views
from virat.forms import UserForm,ProfileInfo


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from virat.forms import NewUser 


# Create your views here.
def index(request):
	my_dict={"insert_me":'This is for 2023'}
	return render(request,'rv.html',context=my_dict)

def kohli(request):
	return render(request,'kohli.html')

def vespa(request):
	return render(request,'basic.html')

def thambi(request):
	dict_my={'text':'hello world','number':10}
	return render(request,'example.html',dict_my)

@login_required
def special(request):
	return HttpResponse("You are Logged in Welcome!")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


# def form_name(request):
# 	form_list = forms.FormName()
# 	return render(request,'forms.html',{'form':form_list})

# def users(request):
# 	form = NewUser()

# 	if request.method == 'POST':
# 		form = NewUser(request.POST)

# 		if form.is_valid():
# 			form.save(commit=True)
# 			return index(request)
# 		else:
# 			print('Invalid')
# 	return render(request,'forms.html',{'form':form})



def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse("Account Not Active")
		else:
			print("Someone Tried to Login and Failed")
			print("Username:{} and password {}".format(username,password))
			return HttpResponse("invalid login details suppiled")

	else:
		return render(request,'virat/login.html',{})
			