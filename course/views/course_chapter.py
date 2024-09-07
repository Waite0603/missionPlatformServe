# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： course_chapter.py
    @date：2024/9/7 下午8:47
    
    TODO:
"""
import hashlib
import json
import os
import time

from django.http import FileResponse

from missionPlatform.decorators import get_only, post_only, login_required
from missionPlatform.utils.response import ResponseInfo
from missionPlatform.utils.token import get_user_info
from missionPlatform.utils.tools import model_to_dict
from ..models import Course, CourseCategory, Chapter


@post_only
@login_required
def create_chapter(request):
  user_data = get_user_info(request)
  try:
    data = json.loads(request.body)
  except json.JSONDecodeError:
    return ResponseInfo.fail(400, 'Invalid JSON')

  course_id = data.get('courseId')
  name = data.get('name')
  video = data.get('video')

  if not all([course_id, name, video]):
    return ResponseInfo.fail(400, '参数不全')

  # 查看课程是否存在
  course_data = Course.objects.filter(id=course_id, status=1).first()
  if not course_data:
    return ResponseInfo.fail(404, '课程不存在')

  # 查看章节是否存在
  chapter_data = Chapter.objects.filter(name=name, course=course_data, status=1).first()

  if chapter_data:
    return ResponseInfo.fail(400, '章节已存在')

  # 创建章节
  Chapter.objects.create(
    name=name,
    video=video,
    course=course_data,
    author=user_data
  )

  # 返回所有章节
  chapter_list = Chapter.objects.filter(course=course_data, status=1).order_by('create_time').values()

  chapter_list = [
    model_to_dict(chapter) for chapter in chapter_list
  ]

  return ResponseInfo.success('创建成功', data=chapter_list)


@get_only
def get_chapter_list(request):
  course_id = request.GET.get('courseId')
  if not course_id:
    return ResponseInfo.fail(400, '参数不全')

  course_data = Course.objects.filter(id=course_id, status=1).first()
  if not course_data:
    return ResponseInfo.fail(404, '课程不存在')

  chapter_list = Chapter.objects.filter(course=course_data, status=1).order_by('create_time').values()

  chapter_list = [
    model_to_dict(chapter) for chapter in chapter_list
  ]

  return ResponseInfo.success('获取成功', data=chapter_list)


@post_only
@login_required
def update_chapter(request):
  try:
    data = json.loads(request.body)
  except json.JSONDecodeError:
    return ResponseInfo.fail(400, 'Invalid JSON')

  chapter_id = data.get('id')
  name = data.get('name')
  video = data.get('video')

  if not all([chapter_id, name, video]):
    return ResponseInfo.fail(400, '参数不全')

  # 查看章节是否存在
  chapter_data = Chapter.objects.filter(id=chapter_id, status=1).first()
  if not chapter_data:
    return ResponseInfo.fail(404, '章节不存在')

  # 更新章节
  chapter_data.name = name
  chapter_data.video = video
  chapter_data.save()

  # 返回所有章节
  chapter_list = Chapter.objects.filter(course=chapter_id, status=1).order_by('create_time').values()

  chapter_list = [
    model_to_dict(chapter) for chapter in chapter_list
  ]

  return ResponseInfo.success('更新成功', data=chapter_list)


@get_only
@login_required
def delete_chapter(request):
  print(request.GET)
  chapter_id = request.GET.get('id')
  if not chapter_id:
    return ResponseInfo.fail(400, '参数不全')

  # 查看章节是否存在
  chapter_data = Chapter.objects.filter(id=chapter_id, status=1).first()
  if not chapter_data:
    return ResponseInfo.fail(404, '章节不存在')

  # 删除章节
  chapter_data.status = 0
  chapter_data.save()

  # 返回所有章节
  chapter_list = Chapter.objects.filter(course=chapter_data.course, status=1).order_by('create_time').values()

  chapter_list = [
    model_to_dict(chapter) for chapter in chapter_list
  ]

  return ResponseInfo.success('删除成功', data=chapter_list)
