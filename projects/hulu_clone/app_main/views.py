from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


def index(request):
    context = {

    }
    return render(request, 'index.html', context)
