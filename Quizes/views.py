from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView

# listview is to list the quizes, we might go for another view later

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'

def Quiz_view(request, id):
    quiz = Quiz.objects.get(pk=id)
    return render(request, 'quizes/quizes.html', {'obj':quiz})