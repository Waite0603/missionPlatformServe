import json

from missionPlatform.decorators import post_only
from missionPlatform.utils.response import ResponseInfo
from missionPlatform.handler import ResponseInfo


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


def login(request):
  """
  用户登录
  :param request:
  :return:
  """
  # 检查 Content-Type 是否为 application/json
  content_type = request.META.get('CONTENT_TYPE', '')
  if content_type != 'application/json':
    return ResponseInfo.fail(400, '请求头错误')
  if request.method == 'POST':
    try:
      data = json.loads(request.body.decode('utf-8'))  # 解码为 UTF-8 字符串
    except json.JSONDecodeError:
      return ResponseInfo.fail(400, '参数错误')

    print(data)

    # 2. 参数校验
    username = data.get('username')
    password = data.get('password')

    if not all([username, password]):
      return ResponseInfo.fail(400, '参数不全')

    # print
    print(username, password)
    return ResponseInfo.success('登录成功')
  else:
    return ResponseInfo.fail(405, '请求方式错误')
