from django.shortcuts import render, render_to_response
from django.contrib.auth import login, get_user_model, logout

from django.http import HttpResponseRedirect
# Create your views here.
from .forms import UserCreationForm, UserLoginForm


def register(request, *args, **kwargs):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/login")
	context = {
		'form': form
	}
	return render(request, "accounts/register.html", context)


def login_view(request, *args, **kwargs):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		uname = request.session.get('username')
		if uname is None:
			user_obj = form.cleaned_data.get('user_obj')
			login(request, user_obj)
			request.session['username'] = user_obj.username
			return HttpResponseRedirect("/profile")
		else:	
			del request.session['username']
			return HttpResponseRedirect("/")
	return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
	try:
		logout(request)
		del request.session['username']
	except:
		pass
	return HttpResponseRedirect("/login")