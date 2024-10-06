# ceo program

from django.shortcuts import render

def robots(request):
    return render(request, 'Piconverterapp/ceo/robot.txt')

def sitemap(request):
    return render (request, 'Piconverterapp/ceo/sitemap.xml', content_type='text/xml, application/xml')

def open_search(request):
    return render (request, 'Piconverterapp/ceo/searchlink.xml', content_type='text.xml, application/xml')

def app_manifest(request):
    return render (request, 'Piconverterapp/ceo/app.json', content_type='application/json')