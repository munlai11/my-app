from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/<slug:slug>/remove/', views.post_remove, name='post_remove'),

    path('post/<int:pk>/<slug:slug>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/<slug:slug>/remove/', views.comment_remove, name='comment_remove'),

    path('post-category-list/', views.category_list, name='category_list'),
    path('post-category-list/<int:pk>/<slug:slug>/role-detail/', views.role_detail, name='role_detail'),
    path('post-category-list/<int:pk>/<slug:slug>/company-detail/', views.company_detail, name='company_detail'),

]