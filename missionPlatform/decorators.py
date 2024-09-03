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
from missionPlatform.utils.token import verify_jwt_token


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


def login_required(view_func):
  # 获取 Authorization
  @wraps(view_func)
  def _wrapped_view(request, *args, **kwargs):
    auth_header = request.headers.get('Authorization')
    # get refresh token
    refresh_token = request.headers.get('Refresh')
    if not auth_header:
      return ResponseInfo.fail(status.HTTP_403_FORBIDDEN, msg='请先登录')

    if not verify_jwt_token(auth_header, refresh_token):
      return ResponseInfo.fail(status.HTTP_403_FORBIDDEN, msg='登录过期, 请重新登录')

    return view_func(request, *args, **kwargs)

  return _wrapped_view