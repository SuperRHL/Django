from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def projects(request):
    return HttpResponse('Here is a list of projects')
    
def project(request, pk):
    return HttpResponse('Here is a project'+' '+ str(pk))
