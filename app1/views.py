from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'sample.html')

def index1(request,data):
    return HttpResponse(f'<h1>the  carried data {data}</h1>')

# Create your views here.
