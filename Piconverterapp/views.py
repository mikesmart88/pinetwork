from django.shortcuts import render,redirect 
from django.http import HttpResponse , JsonResponse

# Create your views here.

def base(request):
    return render(request, 'Piconverterapp/base.html')
