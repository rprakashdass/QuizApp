from django.urls import path
from .views import *
app_name = 'Quizes'

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz_list'),
    path('<id>/',Quiz_view,name='quiz-view'),
]
