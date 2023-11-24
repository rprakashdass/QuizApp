from django.urls import path
from .views import (
    QuizListView,
    Quiz_view,
)

app_name = 'Quizes'
urlpatterns = [
     path('', QuizListView.as_view(), name='quiz_list'),
    path('<pk>/',Quiz_view,name='quiz-view'),
]
