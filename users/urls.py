"""为应用程序users定义url模式"""

from django.urls import path,re_path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
import os

from . import views

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

urlpatterns = [
    #登录界面
    #re_path(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    path(r'login/', LoginView.as_view(template_name='users/login.html'), name='login')
]