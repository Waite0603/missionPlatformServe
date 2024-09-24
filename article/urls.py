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
  re_path(r'^recommend/?$', v.recommend_article, name='recommend_article'),
  re_path(r'^cover/(?P<cover_name>[^/]+)$', v.get_article_cover, name='get_article_cover'),
  re_path(r'^index/?$', v.index_recommend_article, name='index_recommend_article'),
  re_path(r'^search/?$', v.search_article, name='search_article')
]
