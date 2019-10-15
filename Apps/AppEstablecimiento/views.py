from django.shortcuts import render

# Create your views here.
from requests import request


def Home(request):
    return render(request, 'TempEstablecimiento/index.html')