from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def india(request):
    return HttpResponse('<h1>INDIA team is top one cricket team in world</h1>')