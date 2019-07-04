from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.feedback_new, name='feedback_new'),
]