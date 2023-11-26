from django.urls import path
from .views import *
app_name = 'Quizes'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-categories'),
    path('<id>/',Quiz_view,name='quizes'),
    path('<id>/submit/',SubmitView,name='submit'),
    path('<id>/question/',QuestionView,name='questions'),
]
