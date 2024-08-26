import json

from missionPlatform.decorators import post_only, get_only, login_required
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from missionPlatform.utils.response import ResponseInfo
from django.contrib.auth.hashers import check_password
from django.utils import timezone

from missionPlatform.utils.token import create_jwt_pair_for_user
from missionPlatform.utils.tools import model_to_dict
from .models import UserProfileModel
import re


@post_only
def register(request):
  """
  用户注册
  :param request:
  :return:
  """
  try:
    data = json.loads(request.body)
  except json.JSONDecodeError:
    return ResponseInfo.fail(400, 'Invalid JSON')

  username = data.get('username')
  password = data.get('password')
  email = data.get('email')
  phone = data.get('phone')
  verify_code = data.get('verificationCode')

  # 2. 参数校验
  if not all([username, password, email, phone, verify_code]):
    return ResponseInfo.fail(400, '参数不全')

  # 校验邮箱格式
  if not re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email):
    return ResponseInfo.fail(400, '邮箱格式错误')

  # 校验手机号格式
  if not re.match(r'^1[3-9]\d{9}$', phone):
    return ResponseInfo.fail(400, '手机号格式错误')

  # 校验验证码
  if verify_code != '123456':
    return ResponseInfo.fail(400, '验证码错误')

  # 请求数据库，校验用户名、邮箱或手机号是否存在
  user_data = UserProfileModel.objects.filter(
    Q(username=username) | Q(email=email) | Q(phone=phone)
  ).first()

  if user_data:
    if user_data.username == username:
      return ResponseInfo.fail(400, '用户名已存在')
    elif user_data.email == email:
      return ResponseInfo.fail(400, '邮箱已存在')
    elif user_data.phone == phone:
      return ResponseInfo.fail(400, '手机号已存在')

  # 密码加密
  password = make_password(password)

  UserProfileModel.objects.create(username=username, password=password, email=email, phone=phone,
                                  last_login=timezone.now())

  return ResponseInfo.success('注册成功')


@post_only
def login(request):
  """
  用户登录
  :param request:
  :return:
  """
  try:
    data = json.loads(request.body)
  except json.JSONDecodeError:
    return ResponseInfo.fail(400, 'Invalid JSON')

  username = data.get('username')
  password = data.get('password')
  # 2. 参数校验
  if not all([username, password]):
    return ResponseInfo.fail(400, '参数不全')
  # 3. 业务处理
  # 请求数据库，校验用户名和密码
  user_data = UserProfileModel.objects.filter(username=username).first()
  if not user_data or not check_password(password, user_data.password):
    return ResponseInfo.fail(401, '用户名或密码错误')

  # 查询结果转换为字典
  token = create_jwt_pair_for_user(user_data)
  user_data = model_to_dict(user_data)

  # 删除密码
  del user_data['password']
  del user_data['is_staff']
  user_data['token'] = token

  # 更新登录时间
  UserProfileModel.objects.filter(username=username).update(last_login=timezone.now())

  return ResponseInfo.success('登录成功', data=user_data)


@login_required
def logout(request):
  return ResponseInfo.success('登出成功')


# 获取验证码
@get_only
def get_verify_code(request):
  return ResponseInfo.success('123456')
