from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('start/', views.start_quiz, name='start_quiz'),
    path('question/', views.get_question, name='get_question'),
    path('save-answer/', views.save_answer, name='save_answer'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
]
