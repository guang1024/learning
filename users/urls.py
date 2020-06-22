"""为应用程序users定义url模式"""

from django.urls import path
from django.contrib.auth import login

from . import views

urlpatterns = [
    #登录界面
    path(r'login/', login, {'template_name': 'users/login.html'}, name='login')
]