# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： decorators.py
    @date：2024/8/1 下午9:01
    
    TODO: 重写装饰器, 用于限制请求方式
"""
from functools import wraps
from rest_framework import status
from missionPlatform.handler import ResponseInfo


def post_only(view_func):
  @wraps(view_func)
  def _wrapped_view(request, *args, **kwargs):
    if request.method != 'POST':
      return ResponseInfo.fail(status.HTTP_405_METHOD_NOT_ALLOWED, '请求方式错误')
    return view_func(request, *args, **kwargs)

  return _wrapped_view


def get_only(view_func):
  @wraps(view_func)
  def _wrapped_view(request, *args, **kwargs):
    if request.method != 'GET':
      return ResponseInfo.fail(status.HTTP_405_METHOD_NOT_ALLOWED, '请求方式错误')
    return view_func(request, *args, **kwargs)

  return _wrapped_view
