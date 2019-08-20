from django.shortcuts import render

# Create your views here.

def board(request):
    return render(request,'board.html')

def boarddetail(request):
    return render(request,'board_detail.html')

def boardnew(request):
    return render(request,'board_new.html')

def introduce(request):
    return render(request,'introduce.html')

def introdetail(request):
    return render(request,'intro_detail.html')
