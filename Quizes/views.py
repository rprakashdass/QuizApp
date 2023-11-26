from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'

def Quiz_view(request, id):
    quiz = Quiz.objects.get(pk=id)
    return render(request, 'quizes/quizes.html', {'obj':quiz})

def QuestionView(request, id):
    quiz = Quiz.objects.get(pk=id)
    questions = []
    for question in quiz.get_questions():
        answers = []
        for answer in question.get_answers():
            answers.append(answer.text)
        questions.append({str(question.text): answers})
    return JsonResponse({
        'question' : questions,
        'time' : quiz.time,
    })

def SubmitView(request, id):
    if request.is_ajax():
        data = dict(request.POST.lists())
        print(type(data))
        data.pop('csrfmiddlewaretoken')
        print(data)
    return JsonResponse({'text':'works'})