from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
urlpatterns = [
    path('upload/', views.upload_view, name='upload'),
    path('music_files/', views.music_files_view, name='music_files'),
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('logout/',views.user_logout,name='logout'),

]
    # Add other URL patterns if needed
