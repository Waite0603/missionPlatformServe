# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： urls.py
    @date：2024/8/29 下午6:33
    
    TODO:
"""
from django.urls import re_path

from . import views as v

urlpatterns = [
  re_path(r'^add/?$', v.add_article, name='add_article'),
  re_path(r'^get/?$', v.get_article, name='get_article'),
  re_path(r'^get_list/?$', v.get_article_list, name='get_article_list'),
  re_path(r'^update/?$', v.update_article, name='update_article'),
  re_path(r'^delete/?$', v.delete_article, name='delete_article'),

]
