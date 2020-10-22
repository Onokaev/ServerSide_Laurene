from django.shortcuts import render
from . import models
def login(request):
    return render(request, 'login.html', {})

def home(request):
    print(request)
    records = models.SocDoc.objects.values()
    return render(request, 'home.html', {"records": list(records)})
