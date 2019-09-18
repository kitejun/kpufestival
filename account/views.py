from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            messages.warning(request,'아이디가 이미 사용중입니다')
        else:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
                # 계정 생성
                auth.login(request, user)  # 회원가입하면 자동 로그인 될 수 있게
                return redirect('home')  # 로그인되면 home으로
            else:
                messages.warning(request,'비밀번호가 일치하지 않습니다.')

    return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.warning(request,'이메일 or 비밀번호가 일치하지 않습니다.')
            return render(request, 'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')