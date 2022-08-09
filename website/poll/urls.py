from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('stu/', views.stureg, name='stureg'),
    path('tea/', views.teacher_reg, name='teareg'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]
