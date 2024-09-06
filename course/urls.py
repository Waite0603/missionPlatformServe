# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： urls.py
    @date：2024/9/6 上午10:44
    
    TODO:
"""
from django.urls import re_path
from .views import course_category as category
from .views import course

urlpatterns = [
  re_path(r'^category/create/?$', category.create_category, name='create_category'),
  re_path(r'^category/list/?$', category.get_category_list, name='get_category_list'),
  re_path(r'^category/update/?$', category.update_category, name='update_category'),
  re_path(r'^category/delete/?$', category.delete_category, name='delete_category'),

  re_path(r'^create/?$', course.create_course, name='create_course'),
  re_path(r'^list/?$', course.get_course_list, name='get_course_list'),


]
