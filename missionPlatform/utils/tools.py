# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： tools.py
    @date：2024/8/16 下午12:47
"""


# 将数据库 filter 的结果转换为字典
def model_to_dict(obj):
  """
  将数据库 filter 的结果转换为字典
  :param obj: 数据库查询结果
  :return: 字典
  """
  if obj is None:
    return None
  if isinstance(obj, list):
    return [model_to_dict(o) for o in obj]
  if isinstance(obj, dict):
    return {k: model_to_dict(v) for k, v in obj.items()}
  if hasattr(obj, '__dict__'):
    return {k: model_to_dict(v) for k, v in obj.__dict__.items() if not k.startswith('_')}
  return obj
