from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('posts.urls')),
    path('', include('questions.urls')),
    path('', include('search.urls')),
    path('', include('interviews.urls')),
    path('', include('comms.urls')),
    path('', include('home.urls')),
    path('', include('video.urls')),
    url(r'^chat/', include('chat.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
