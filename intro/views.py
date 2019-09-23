from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

from .models import Intro

import random

def firework(request):
    return render(request,'firework.html')

def introduce(request):
    # random 으로 학과 주점 보여주기
    all_intro=Intro.objects.annotate().order_by('?')

    random_button = random.randint(1, 2)
    random_width = random.randint(20, 80)
    random_height = random.randint(20, 80)

    return render(request,'introduce.html', { 'all_intro':all_intro, 'random_button': random_button, 'random_width': random_width, 'random_height': random_height })

def intro_detail(request, intro_id):
    intro_detail = get_object_or_404(Intro, pk=intro_id)
    # 타 학과
    exclude_intro=Intro.objects.annotate().order_by('?').exclude(id = intro_id)

    random_button = random.randint(1, 2)
    random_width = random.randint(20, 80)
    random_height = random.randint(20, 80)

    return render(request,'intro_detail.html', {'intro_detail': intro_detail, 'exclude_intro': exclude_intro, 'random_button': random_button, 'random_width': random_width, 'random_height': random_height})


def intro_like(request, intro_id):
    # 로그인 안 되어있을 때 로그인 페이지로
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        
    intro = get_object_or_404(Intro, id=intro_id)
    if request.user in intro.intro_like_users.all():
        intro.intro_like_users.remove(request.user)
    else:
        intro.intro_like_users.add(request.user)
    return redirect('/intro/intro_detail/' + str(intro.id))
