from django.urls import path
from . import views

urlpatterns = [
    path('interview/new/', views.interview_new, name='interview_new'),
    path('search/interviews',views.interview_list, name='interview_list'),
    path('interview/<int:pk>/<slug:slug>/', views.interview_detail, name='interview_detail'),
    path('interview/<int:pk>/<slug:slug>/accept/',views.interview_accept, name='interview_accept'),
    path('interview/<int:pk>/<slug:slug>/cancel/',views.interview_cancel, name='interview_cancel')
]