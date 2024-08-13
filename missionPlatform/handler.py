# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： local_settings.py
    @date：2024/8/1 下午5:31

    TODO: 重写 ResponseInfo 类, 用于返回响应信息
"""
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class ResponseInfo(Response):
  def __init__(self, code=200, data=None, headers=None, content_type=None, **kwargs):
    dic = {
      'code': code,
      'data': data
    }

    if data is not None:
      dic['data'] = data

    dic.update(kwargs)
    super().__init__(dic, status=code, headers=headers, content_type=content_type)
    self.accepted_renderer = JSONRenderer()
    self.accepted_media_type = self.accepted_renderer.media_type
    self.renderer_context = {}

  @classmethod
  def success(cls, data=None, **kwargs):
    return cls(code=200, data=data, **kwargs)

  @classmethod
  def fail(cls, code, data=None, **kwargs):
    return cls(code=code, data=data, **kwargs)
