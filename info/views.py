from django.shortcuts import render

def temp(request):
    return render(request, 'temp.html')
    
def home(request):
    return render(request, 'home.html')

def developer(request):
    return render(request,'developer.html')

def siru(request):
    return render(request,'siru.html')

def promote(request):
    return render(request,'promote.html')