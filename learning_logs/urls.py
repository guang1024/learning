'''定义learning_logs的URL模式'''

from django.urls import path

from . import views

urlpatterns = [
    # 主页
    #错误:path(r'^$', views.index, name='index'),    #不匹配正则
    path(r'', views.index, name='index'),
    #显示所有的主题
    path(r'^topics/$', views.topics, name='topics'),
]