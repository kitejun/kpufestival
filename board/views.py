from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import auth
# 파일 저장 import문
from django.core.files.storage import FileSystemStorage

from .models import Board, Comment, Missing
from .forms import BoardPost, MissingPost
from django.views.generic.edit import FormView
from django.db.models import Q

# 메세지 라이브러리
from django.contrib import messages

from django.conf import settings
from django.shortcuts import render

# 게시판 카테고리 별 순서
from django.db.models import Count

from django.db.models import Max 

#===================================================================================================================
# 게시판
def board(request):
    boards=Board.objects

    # 댓글 수
    counts=Board.objects.count()

    board_list=Board.objects.all()
        
    #페이지
    paginator = Paginator(board_list,5)
    total_len=len(board_list)

    page = request.GET.get('page',1)
    posts = paginator.get_page(page)
    
    try:
        lines = paginator.page(page) 
    except PageNotAnInteger: 
        lines = paginator.page(1) 
    except EmptyPage: 
        lines = paginator.page(paginator.num_pages) 
        
    index = lines.number -1 
    max_index = len(paginator.page_range) 
    start_index = index -2 if index >= 2 else 0 
    if index < 2 : 
        end_index = 5-start_index
    else : 
        end_index = index+3 if index <= max_index - 3 else max_index 
    page_range = list(paginator.page_range[start_index:end_index]) 
    
    context = { 'boards':boards,'board_list': lines ,'counts':counts, 'posts':posts, 'page_range':page_range, 'total_len':total_len, 'max_index':max_index-2 } 
    return render (request,'board.html', context )


def board_detail(request, board_id):
    details = get_object_or_404(Board, pk=board_id)
    return render(request, 'board_detail.html', {'details': details})

def new(request):
    # 로그인 안 되어있을 때 로그인 페이지로
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BoardPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # DB에 저장하지 않고 form에 임시 저장
            post.author=request.user
            # 날짜는 자동으로 현재 입력해주는 것
            post.pub_date = timezone.now()
            post.save()
            return redirect('board')     # 바로 home으로 redirect
        
        else: #아무것도 안쓰고 글쓰기 눌렀을 때
            messages.info(request, '내용을 입력하세요!')
            return redirect('new')
    
    # 2. 빈 페이지를 띄어주는 기능 -> GET
    else:
        form = BoardPost()
        return render(request, 'board_new.html', {'form':form}) # form형태로 전달

# 수정하기
def update(request,board_id):
    post=Board.objects.get(id=board_id)

    # 글을 수정사항을 입력하고 제출을 눌렀을 때
    if request.method == "POST":
        form = BoardPost(request.POST, request.FILES)
        if form.is_valid():
                
            # 검증에 성공한 값들은 사전타입으로 제공 
            print(form.cleaned_data)
            post.title = form.cleaned_data['title']
            post.context = form.cleaned_data['context']
            post.image = form.cleaned_data['image']
            post.pub_date = timezone.now()

            post.save()
            
            return redirect('board')

    # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
    else:
        form = BoardPost(instance = post)
        # 기존 내용 불러오기
        context={
            'form':form,
            'writing':True,
            'now':'update',
        }
        return render(request, 'update.html',{'form':form})

# 삭제하기
def delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    board.delete()
    return redirect('board')

def like(request, board_id):
    # 로그인 안 되어있을 때 로그인 페이지로
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    board = get_object_or_404(Board, id=board_id)
    if request.user in board.like_users.all():
        board.like_users.remove(request.user)
    else:
        board.like_users.add(request.user)
    return redirect('/board/board_detail/' + str(board.id))

def hate(request, board_id):
    # 로그인 안 되어있을 때 로그인 페이지로
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        
    board = get_object_or_404(Board, id=board_id)
    if request.user in board.hate_users.all():
        board.hate_users.remove(request.user)
    else:
        board.hate_users.add(request.user)
    return redirect('/board/board_detail/' + str(board.id))

#===================================================================================================================
# 댓글
def comment_write(request, board_id):
    # 로그인 안 되어있을 때 로그인 페이지로
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        
    if request.method == 'POST':
        board = get_object_or_404(Board, pk=board_id)
        content = request.POST.get('content')
        author_user=request.user
        Comment.objects.create(board=board, comment_body=content, author=author_user)
        return redirect('/board/board_detail/' + str(board.id))
    
# 댓글 삭제하기
def comment_delete(request,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    # return redirect('/board/detail/' + 'str(comment.id)')
    # return redirect('/board/detail/', comment_id=comment.board.id)
    return redirect('/board')

def comment_like(request, comment_id):
    # 로그인 안 되어있을 때 로그인 페이지로
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.comment_like_users.all():
        comment.comment_like_users.remove(request.user)
    else:
        comment.comment_like_users.add(request.user)
    return redirect('/board')

def comment_hate(request, comment_id):
    # 로그인 안 되어있을 때 로그인 페이지로
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.comment_hate_users.all():
        comment.comment_hate_users.remove(request.user)
    else:
        comment.comment_hate_users.add(request.user)
    return redirect('/board')

#===================================================================================================================
# 분실물
def missing(request):
    missings=Missing.objects.all()

    # 댓글 수
    counts=Missing.objects.count()
        
    return render (request,'missing.html', { 'missings':missings, 'counts':counts } )


def missing_detail(request, missing_id):
    missing_details = get_object_or_404(Missing, pk=missing_id)
    return render(request, 'missing_detail.html', {'missing_details': missing_details})

def missing_new(request):
    # 로그인 안 되어있을 때 로그인 페이지로
    if not request.user.email.endswith('@naver.com'):
        return redirect('missing')

    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = MissingPost(request.POST, request.FILES)
        if form.is_valid():
            missing = form.save(commit=False) # DB에 저장하지 않고 form에 임시 저장
            missing.author=request.user
            # 날짜는 자동으로 현재 입력해주는 것
            missing.pub_date = timezone.now()
            missing.save()
            return redirect('missing')     # 바로 home으로 redirect
        
        else: #아무것도 안쓰고 글쓰기 눌렀을 때
            messages.info(request, '내용을 입력하세요!')
            return redirect('missing_new')
    
    # 2. 빈 페이지를 띄어주는 기능 -> GET
    else:
        form = MissingPost()
        return render(request, 'missing_new.html', {'form':form}) # form형태로 전달
