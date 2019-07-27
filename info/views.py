from django.shortcuts import render

def temp(request):
    return render(request, 'temp.html')
    
def home(request):
    return render(request, 'home.html')