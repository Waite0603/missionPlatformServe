# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： urls.py
    @date：2024/6/19 上午11:45
"""
from django.urls import re_path
from . import views as v

urlpatterns = [
  re_path(r'^register/?$', v.register, name='register'),
  re_path(r'^login/?$', v.login, name='login'),
  re_path(r'^logout/?$', v.logout, name='logout'),
  re_path(r'^captcha/?$', v.get_verify_code, name='get_verify_code'),
]
