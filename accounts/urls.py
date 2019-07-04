from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/<int:pk>/<username>/', views.view_profile, name='view_profile'),
    path('profile/<int:pk>/<username>/edit', views.edit_profile, name='edit_profile'),
    path('profile/<int:pk>/<username>/details/edit', views.edit_details, name='edit_details'),

]