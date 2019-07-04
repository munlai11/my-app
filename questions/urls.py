from django.urls import path
from . import views

urlpatterns = [
        path('question/new/', views.question_new, name='question_new'),
        path('search/questions',views.question_list, name='question_list'),
        path('question/<int:pk>/<slug:slug>/part/new/', views.question_part_new, name='question_part_new'),
        path('question/<int:pk>/<slug:slug>/', views.question_detail, name='question_detail'),
        path('question/<int:pk>/<slug:slug>/remove/', views.question_remove, name='question_remove'),
        path('question/<int:pk>/<slug:slug>/like/', views.like_question, name='like_question'),
]