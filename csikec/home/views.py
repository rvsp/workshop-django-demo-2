from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

def home_view(request):
        return render(request, "home.html")


def userProfile(request):
        if request.session.has_key('username'):
                username = request.session['username']
                user_obj = User.objects.filter(
                        Q(username__iexact=username)).distinct()
                if not user_obj.exists() and user_obj.count != 1:
                        return ValueError('User Logout')
                else:
                        context = {
                                "user_obj":user_obj,
                        }
                return render(request, "accounts/ViewUserProfile.html",context)
        else:
                return HttpResponseRedirect('/login')
