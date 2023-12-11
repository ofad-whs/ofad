from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


"""
 * API No. 1
 * API Name : 게시글 불러오기
 * [GET] /noticeBoard
"""
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'noticeBoard/question_list.html', context)


"""
 * API No. 2
 * API Name : 게시글 상세 조회
 * [GET] /noticeBoard/{boardId}
"""

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'noticeBoard/question_detail.html', context)


"""
 * API No. 3
 * API Name : 댓글 작성
 * [POST] /noticeBoard/answer/create/{answerID}
"""
@login_required(login_url='user:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now(), author=request.user)
    return redirect('noticeBoard:detail', question_id=question.id)


"""
 * API No. 4
 * API Name : 게시글 작성
 * [GET] /noticeBoard/question/create
"""
@login_required(login_url='user:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date=timezone.now()
            question.save()
            return redirect('noticeBoard:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'noticeBoard/question_form.html', context)

"""
 * API No. 5
 * API Name : 게시글 삭제
 * [GET] /noticeBoard/question/delete
"""
##@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('noticeBoard:detail', question_id=question.id)
    question.delete()
    return redirect('noticeBoard:index')

"""
 * API No. 6
 * API Name : 댓글 삭제
 * [GET] /noticeBoard/answer/delete
"""
##@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('noticeBoard:detail', answer_id=answer.id)
    answer.delete()
    return redirect('noticeBoard:index')
