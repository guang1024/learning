"""为应用程序users定义url模式"""

from django.urls import path,re_path
from django.contrib.auth import login

from . import views

urlpatterns = [
    #登录界面
    path(r'login/', login, 'users/login.html', name='login'),
]