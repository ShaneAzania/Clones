from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import bcrypt

from app_main.static.modules.nav import nav_render
from .models import User



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
    post = request.POST
    which_form = post['which_form']
    # Login form
    if which_form == 'login':
        email = post['email']
        password = post['password']
        # bcrypt.checkpw('test'.encode(), hashed_PW_from_DB.encode())

        print()
        print('Login:')
        print()
        return HttpResponse('User Logged In')
    # Signup form
    elif which_form == 'signup':
        # validate form data
        errors = User.objects.signup_validator(post)
        if not errors:
            print()
            print('Signup: Valid')
            print()
            # check if email is already registered
            existing_user = User.objects.filter(email = post['email'])
            if len(existing_user) > 0:
                messages.error(request, 'That email is already registered to an existing user.')
                return redirect("/login_signup")
            # hash password and creare user
            bcrypted_password = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt()).decode()
            # create user
            User.objects.create(email = post['email'].lower(), first_name = post['first_name'], last_name = post['last_name'], password = bcrypted_password)
            # put user data into session
            current_user = User.objects.get(email = post['email'])
            request.session['user'] = {
                'id' : current_user.id,
                'email' : current_user.email,
                'first_name' : current_user.first_name,
                'last_name' : current_user.last_name,
            }
            return HttpResponse('User Created' + request.session['user']['email'])
        elif errors:
            # load errors into messages
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/login_signup")

def logout(request):
    del request.session['user']
    return redirect("/login_signup")

def user_dash(request):
    context = {
        'nav' : nav_render(request),
    }
    return render(request, 'user_dash.html', context)
