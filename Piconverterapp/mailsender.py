
""" 
Code for sending email to google account using api key from app.Brevo.com,
by sendin a post request to this url: https://api.mailersend.com/v3/smtp/email
Python configuration for sending the mail through mailserder

"""
import requests

def send_mail(recipient_email,mail_info,mail_subj,sender_name):

    # Mailersend Api endpoint for sending transactional email..
    
    url = 'https://api.mailersend.com/v3/smtp/email'

    # The the email data we are sending to the user...

    mailer = {
        "sender":{
            "name": f"Micheal",
            "email": "uzomamicheal07@gmail.com"
        },
        "to":[
             {
                "email":recipient_email,
                "name":f"{sender_name}"
            }
        ],
        "subjects":f"{mail_subj}",
        "html content":f"{mail_info}"
    }

    # Our authorized header
    headers = {
        'api_token':"mlsn.d5bb187e12444667a20ca5e8fb4c69704af635fbf23d7386a8854cd19ad970e1",
        'content-Type':'application/json',
        'accept':'application/json',
    }

    # Our post request
    response = requests.post(url,json=mailer,headers=headers)
    return True


