# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： urls.py
    @date：2024/9/30 下午4:25
    
    TODO:
"""
from django.urls import re_path
import comment.views as views

urlpatterns = [
  re_path(r'^create/?$', views.create_comment, name='create_comment'),
  re_path(r'^list/?$', views.get_comment, name='get_comment_list'),
]
