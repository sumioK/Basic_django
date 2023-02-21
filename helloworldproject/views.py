from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(req):
    returnedobject = HttpResponse('<h1>hello world .</h1>')
    print('This is hello page')
    return returnedobject

class HelloworldClass(TemplateView):
    template_name = 'hello.html'