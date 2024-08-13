# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： response.py
    @date：2024/6/19 上午11:36
"""
from django.http import JsonResponse


class ResponseInfo:
  def __init__(self, code, msg, data=None):
    self.code = code
    self.msg = msg
    self.data = data

  def to_json_response(self):
    """
    返回一个 JsonResponse 对象。
    """
    if self.data is None:
      return JsonResponse({
        "code": self.code,
        "msg": self.msg
      })
    return JsonResponse({
      "code": self.code,
      "msg": self.msg,
      "data": self.data
    })

  # get
  @classmethod
  def success(cls, msg, data=None):
    if data is None:
      return cls(200, msg).to_json_response()
    return cls(200, msg, data).to_json_response()

  @classmethod
  def fail(cls, code, msg, data=None):
    if data is None:
      return cls(code, msg).to_json_response()
    return cls(code, msg, data).to_json_response()
