from django.contrib import admin
from django.urls import path
from . import views as v

#creat your urls here

urlpatterns = [
    path('' ,v.base ,name='viewtime') ,
]