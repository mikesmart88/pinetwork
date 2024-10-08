from django.contrib import admin
from django.urls import path
from . import views as v

#creat your urls here

app_name = 'Piconverterapp'
urlpatterns = [
    path('' ,v.home ,name='homepage') ,
    path('documentation/', v.document, name='piconverter documentation') ,
    path('wallet/', v.wallet, name='pi wallet') ,
    path('exchange/', v.exchange, name='exchage option') ,
]