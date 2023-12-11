from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from reviewBoard.forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.core.paginator import Paginator  
from django.contrib.auth.decorators import login_required

"""
 * API No. 1
 * API Name : 리뷰 불러오기 (리스트)
 * [GET] /reviewBoard
"""
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    review_list = Review.objects.order_by('-create_date')
    paginator = Paginator(review_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj}
    return render(request, 'reviewBoard/review_list.html', context)

"""
 * API No. 2
 * API Name : 리뷰 조회
 * [GET] /reviewBoard/{reviewID}
"""
def detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'reviewBoard/review_detail.html', context)

"""
 * API No. 3
 * API Name : 댓글 작성
 * [POST] reviewBoard/comment/create/{reviewID}
"""
@login_required(login_url='user:login')
def comment_create(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # author 속성에 로그인 계정 저장
            comment.create_date = timezone.now()
            comment.review = review
            comment.save()
            return redirect('reviewBoard:detail', review_id=review.id)
    else:
        form = CommentForm()
    context = {'review': review, 'form': form}
    return render(request, 'reviewBoard/review_detail.html', context)

"""
 * API No. 4
 * API Name : 리뷰 작성
 * [POST] /reviewBoard/review/create
"""
@login_required(login_url='user:login')
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)  #파일 첨부를 위해 request.FILES추가
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  # author 속성에 로그인 계정 저장
            review.create_date = timezone.now()
            review.save()
            return redirect('reviewBoard:index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'reviewBoard/review_form.html', context)

"""
 * API No. 5
 * API Name : 리뷰 삭제
 * [DELETE] reviewBoard/review/delete/{reviewID}
"""
def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('reviewBoard:index')



"""
 * API No. 6
 * API Name : 댓글 삭제
 * [GET] /noticeBoard/answer/delete
"""
##@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('noticeBoard:detail', comment_id=comment.id)
    comment.delete()
    return redirect('reviewBoard:index')