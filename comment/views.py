import json

from django.shortcuts import render

from article.models import Article
from course.models import Course
from missionPlatform.decorators import post_only, login_required, get_only
from missionPlatform.utils.response import ResponseInfo
from missionPlatform.utils.token import get_user_info
from missionPlatform.utils.tools import model_to_dict

from .models import CourseComment
from users.models import UserProfileModel


# 发布评论
@post_only
@login_required
def create_comment(request):
  user_data = get_user_info(request)

  try:
    data = json.loads(request.body)
  except json.JSONDecodeError:
    return ResponseInfo.fail(400, 'Invalid JSON')

  content = data.get('content')
  course_id = data.get('courseId')

  # 查看课程是否存在
  course = Course.objects.filter(id=course_id).first()

  if not course:
    return ResponseInfo.fail(404, '文章不存在')

  if not all([content, course_id]):
    return ResponseInfo.fail(400, '参数不全')

  # 保存评论
  CourseComment.objects.create(
    content=content,
    course=course,
    author=user_data
  )

  # 返回评论
  comment_data = CourseComment.objects.filter(course=course).order_by('-create_time').values()

  # 添加作者名字, 头像
  comment_list = [
    model_to_dict(comment) for comment in comment_data
  ]

  for comment_dict in comment_list:
    user = UserProfileModel.objects.filter(id=comment_dict['author_id']).first()
    comment_dict['author'] = user.username
    comment_dict['avatar'] = user.avatar

  return ResponseInfo.success('新增评论成功', comment_list)


# 获取课程评论
@get_only
def get_comment(request):
  course_id = request.GET.get('courseId')

  if not course_id:
    return ResponseInfo.fail(400, '参数不全')

  course = Course.objects.filter(id=course_id).first()

  if not course:
    return ResponseInfo.fail(404, '课程不存在')

  comment_data = CourseComment.objects.filter(course=course).order_by('-create_time').values()

  comment_list = [
    model_to_dict(comment) for comment in comment_data
  ]

  for comment_dict in comment_list:
    user = UserProfileModel.objects.filter(id=comment_dict['author_id']).first()
    comment_dict['author'] = user.username
    comment_dict['avatar'] = user.avatar

  return ResponseInfo.success('获取评论成功', comment_list)
