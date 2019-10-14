from django.shortcuts import render, redirect
from .models import Question, Choice
import random

# Create your views here.
def index(request):
    questions = Question.objects.all()
    question_ids = []
    for question in questions:
        question_ids.append(question.id)
    q_id = random.choice(question_ids)
    question = Question.objects.get(id=q_id)
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices' : choices,
    }
    return render(request, 'index.html', context)

def question_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        option_left = request.POST.get('option-left')
        option_right = request.POST.get('option-right')

        Question.objects.create(
            title = title,
            option_left = option_left,
            option_right = option_right,
        )
        return redirect('questions:index')
    else:
        return render(request, 'form.html')

def detail(request, question_id, choice_id):
    question = Question.objects.get(id=question_id)
    choices = question.choice_set.all()
    left = 0
    for choice in choices:
        if choice.pick == 1:
            left += 1
    total = len(choices)
    right = total - left
    left_per = round(left / total * 100, 1)
    right_per = round(right / total * 100, 1)
    choice = Choice.objects.get(id=choice_id)
    context = {
        'question': question,
        'left': left,
        'right': right,
        'left_per': left_per,
        'right_per': right_per,
        'choice': choice,
        'choices': choices,
    }
    return render(request, 'detail.html', context)

def pick_count(request, question_id, pick_num):
    question = Question.objects.get(id=question_id)
    pick_num = pick_num
    choice = Choice.objects.create(
        question = question,
        pick = pick_num,
    )
    return redirect('questions:detail', question_id, choice.id)

def answer_create(request, question_id, choice_id):
    choice = Choice.objects.get(id=choice_id)
    comment = request.POST.get('comment')
    choice.comment = comment
    choice.save()
    return redirect('questions:detail', question_id, choice_id)

def question_update(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        title = request.POST.get('title')
        option_left = request.POST.get('option-left')
        option_right = request.POST.get('option-right')

        question.title = title
        question.option_left = option_left
        question.option_right = option_right
        question.save()
        return redirect('questions:index')
    else:
        context = {
            'question': question,
        }
        return render(request, 'question_edit.html', context)

def question_delete(request, question_id):
    question = Question.objects.get(id=question_id)
    question.delete()
    return redirect('questions:index')

def answer_delete(request, question_id, choice_id):
    choice_del = Choice.objects.get(id=choice_id)
    choice_del.delete()
    question = Question.objects.get(id=question_id)
    choice_ids = []
    choices = question.choice_set.all()
    for choice_pick in choices:
        choice_ids.append(choice_pick.id)
    c_id = random.choice(choice_ids)
    return redirect('questions:detail', question_id, c_id)