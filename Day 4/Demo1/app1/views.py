from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HTML_View(request):
    return render(request,'Hello.html')