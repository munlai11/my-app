from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/<slug:slug>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/<slug:slug>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/<slug:slug>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/<slug:slug>/like/', views.like_post, name='like_post'),
    path('comment/<int:pk>/like/', views.like_comment, name='like_comment'),
]