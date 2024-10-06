from django.contrib import admin
from django.urls import path
from . import views as v

#creat your urls here

urlpatterns = [
    path('' ,v.home ,name='homepage') ,
    path('documentation/', v.document, name='piconverter documentation') ,
    path('wallet/', v.wallet, name='pi wallet')
]