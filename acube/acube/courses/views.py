from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
def web(request):
    return HttpResponse("<h1>Welcome to web development</h1><br> this is web development <br><button style = font-size: 12px;>python course</button>")

def pyt(request):
    return HttpResponse('<h1>Welcome to python </h1><br> this is python ')

def datasci(request):
    return HttpResponse('<h1>Welcome to datascience</h1><br> this is datascience')
