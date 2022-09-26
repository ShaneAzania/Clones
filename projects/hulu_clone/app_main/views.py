from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from app_main.static.modules.nav import nav_render



def index(request):
    context = {
        'nav' : nav_render(request),
    }
    return render(request, 'index.html', context)

def login_signup(request):
    context = {
        'nav' : nav_render(request),
    }
    return render(request, 'login_signup.html', context)
def login_signup_form(request):
    context = {
        'nav' : nav_render(request),
    }
    return redirect("/user_dash")

def user_dash(request):
    context = {
        'nav' : nav_render(request),
    }
    return render(request, 'user_dash.html', context)
