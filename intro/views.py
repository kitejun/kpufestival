from django.shortcuts import render, get_object_or_404, redirect


def introduce(request):
    return render(request,'introduce.html')

def intro_detail(request):
    return render(request,'intro_detail.html')

# introduce 기능
# introduce-학과명,좋아요개수,위치,소개글 표시/모달에서 지도 표시
# intro_detail
# -학과명,좋아요 개수,싫어요 개수,조회수,태그,소개글,학과 아이콘 표시/모달에서 지도 표시
# -카톡 공유하기 기능(학과명,사진 공유 혹은 링크)#

