from django.shortcuts import render,redirect
from django.http import HttpResponse , JsonResponse

# Create your views here.

def vd(request):
    return(request, HttpResponse('hello')),
