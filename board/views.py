from django.shortcuts import render

# Create your views here.

def board(request):
    return render(request,'board.html')

def detail(request):
    return render(request,'detail.html')
def introduce(request):
    return render(request,'introduce.html')
