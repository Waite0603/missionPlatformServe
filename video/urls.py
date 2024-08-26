# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： urls.py
    @date：2024/8/25 下午7:38
    
    TODO:
"""
from django.urls import re_path

from . import views as v

urlpatterns = [
  re_path(r'^upload/?$', v.upload_video, name='upload_video'),
  # 获取视频播放链接
  re_path(r'^get/?$', v.get_video, name='get_video'),
]
