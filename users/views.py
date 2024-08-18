from missionPlatform.decorators import post_only, get_only, login_required
from missionPlatform.utils.response import ResponseInfo
from django.contrib.auth.hashers import check_password
from django.utils import timezone

from missionPlatform.utils.token import create_jwt_pair_for_user
from missionPlatform.utils.tools import model_to_dict
from .models import UserProfileModel


@post_only
def register(request):
  """
  用户注册
  :param request:
  :return:
  """
  username = request.POST.get('username')
  password = request.POST.get('password')
  email = request.POST.get('email')
  # 2. 参数校验
  if not all([username, password, email]):
    return ResponseInfo.fail(400, '参数不全')
  # 3. 业务处理
  # 4. 返回响应
  return ResponseInfo.success('注册成功')


@post_only
def login(request):
  """
  用户登录
  :param request:
  :return:
  """
  username = request.POST.get('username')
  password = request.POST.get('password')
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
  user_data['token'] = token

  # 更新登录时间
  UserProfileModel.objects.filter(username=username).update(last_login=timezone.now())

  return ResponseInfo.success('登录成功', data=user_data)


@login_required
def logout(request):
  return ResponseInfo.success('登出成功')
