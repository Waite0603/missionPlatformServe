# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： course.py
    @date：2024/9/6 上午10:44
    
    TODO:
"""
import json

from missionPlatform.decorators import get_only, post_only, login_required
from missionPlatform.utils.response import ResponseInfo
from missionPlatform.utils.token import get_user_info
from missionPlatform.utils.tools import model_to_dict
from ..models import Course, CourseCategory


@post_only
@login_required
def create_course(request):
  try:
    data = json.loads(request.body)
  except json.JSONDecodeError:
    return ResponseInfo.fail(400, 'Invalid JSON')

  name = data.get('name')
  desc = data.get('desc')
  cover = data.get('cover')
  category = data.get('category')

  if not all([name, desc, cover, category]):
    return ResponseInfo.fail(400, '参数不全')

  # 查看课程是否存在
  course_data = Course.objects.filter(name=name).first()
  if course_data:
    return ResponseInfo.fail(400, '课程已存在')

  # 查看分类是否存在
  category_data = CourseCategory.objects.filter(name=category).first()
  if not category_data:
    return ResponseInfo.fail(400, '分类不存在')

  # 创建课程
  Course.objects.create(
    name=name,
    desc=desc,
    cover=cover,
    category=category_data,
    author=get_user_info(request)
  )

  course_list = Course.objects.all().order_by('-create_time').values()

  course_list = [
    model_to_dict(course) for course in course_list
  ]
  return ResponseInfo.success('创建成功', data=course_list)


@get_only
def get_course_list(request):
  course_list = Course.objects.all().order_by('-create_time').values()

  course_list = [
    model_to_dict(course) for course in course_list
  ]

  return ResponseInfo.success('获取成功', data=course_list)
