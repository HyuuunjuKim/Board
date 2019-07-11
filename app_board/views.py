from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def home(request) :
    posts = Board.objects #admin의 Board안의 데이터들을 boards라는 변수에 담음
    post_list = Board.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)
    return render(request, 'home.html', {'posts': posts, 'page_posts' : page_posts})

def detail(request, post_id) :
    post_detail = get_object_or_404(Board, pk = post_id) #pk는 모델에서 찍어낸 객체 구분자
    comments = Comment.objects.filter(board = board.id)
    return render(request, 'detail.html', {'post' : post_detail, 'comments' :comments })

def new(request) :
    return render(request, 'new.html')

def create(request) :
    post = Board()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.writer = request.GET['writer']
    post.save()
    return redirect('/board/' + str(post.id)) #redirect는 요청이 오면 저쪽 url로 보내줘

def delete(request, post_id) :
    delete_post = Board.objects.get(id=post_id)
    delete_post.delete()
    return redirect('home')

def edit(request, post_id) :
    edit_post = Board.objects.get(id=post_id)
    return render(request, 'edit.html', {'post' : edit_post})

def update(request, post_id) :
    update_post = Board.objects.get(id = post_id)
    update_post.title = request.POST['title']
    update_post.body = request.POST['body']
    update_post.writer = request.POST['writer'] 
    update_post.save()
    return redirect('home')
