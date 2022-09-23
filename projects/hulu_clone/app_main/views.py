from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from app_main.static.assets.nav import nav_render



def index(request):
    context = {
        'nav' : nav_render(request),
        'array_1' : ['some thing', 1993, 'another thing'],
    }
    return render(request, 'index.html', context)
