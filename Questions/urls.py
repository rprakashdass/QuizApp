# questions/urls.py

from django.urls import path
from .views import get_questions, submit_answers

app_name = 'questions'

urlpatterns = [
    path('<int:id>/question/', get_questions, name='get-questions'),
    path('<int:id>/submit/', submit_answers, name='submit-answers'),
    # Add other question-related views here if needed
]
