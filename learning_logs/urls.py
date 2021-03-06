'''定义learning_logs的URL模式'''

from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    # 主页
    #错误:path(r'^$', views.index, name='index'),    #不匹配正则
    path(r'', views.index, name='index'),
    #显示所有的主题
    path(r'topics/', views.topics, name='topics'),
    #re_path(r'^topics/$', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #新加主题
    path(r'new_topic/', views.new_topic, name='new_topic'),
    #新加主题条目
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #编辑条目
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]