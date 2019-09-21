from django.shortcuts import render_to_response, render
from django.template import RequestContext
import random

def temp(request):
    return render(request, 'temp.html')
    
def home(request):
    return render(request, 'home.html')

def developer(request):
    random_button = random.randint(1,2)
    random_width = random.randint(20,80)
    random_height = random.randint(20,80)
    # random_button = 2
    return render(request,'developer.html', {'random_button':random_button, 'random_width':random_width, 'random_height':random_height})

def siru(request):
    return render(request,'siru.html')

def promote(request):
    return render(request,'promote.html')

#
'''
def error404(request):
    return render(request, "page_404.html", status=404)

def error500(request):
    return render(request, "page_500.html", status=500)
    '''