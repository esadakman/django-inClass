from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def fshome(request):
    return HttpResponse('<h2>Django!  Django, have you never loved again?<h2>')
    