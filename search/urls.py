from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.category_list, name='category_list'),
    path('search/<int:pk>/<slug:slug>/industry-detail/', views.industry_detail, name='industry_detail'),
    path('search/<int:pk>/<slug:slug>/role-detail/', views.role_detail, name='role_detail'),
    path('search/<int:pk>/<slug:slug>/company-detail/', views.company_detail, name='company_detail'),
]