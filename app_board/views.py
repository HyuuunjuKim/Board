from django.shortcuts import render, get_object_or_404
from .models import Board

# Create your views here.

def home(request) :
    boards = Board.objects #admin의 Board안의 데이터들을 boards라는 변수에 담음
    return render(request, 'home.html', {'posts': boards})

def detail(request, post_id) :
    post_detail = get_object_or_404(Board, pk = post_id) #pk는 모델에서 찍어낸 객체 구분자
    return render(request, 'detail.html', {'post' : post_detail})