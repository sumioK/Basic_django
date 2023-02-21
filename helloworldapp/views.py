from django.shortcuts import render
from django.http import HttpResponse

def helloworldappview(req):
    res = HttpResponse('HelloWorldApp is called!!')
    return res