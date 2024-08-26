import os
import time

from django.shortcuts import render

# Create your views here.
# 上传视频
from django.http import JsonResponse, FileResponse

from missionPlatform.decorators import post_only, login_required
from missionPlatform.utils.token import get_user_info
from missionPlatform.utils.tools import model_to_dict
from video.models import Video, Category, UploadRecord
from missionPlatform.utils.response import ResponseInfo
import hashlib


@post_only
@login_required
def upload_video(request):
  """
  上传视频
  :param request:
  :return:
  """
  user_data = get_user_info(request)

  file_obj = request.FILES.get('file')
  print(file_obj)

  if not file_obj:
    return ResponseInfo.fail(400, '请上传视频')

  upload_dir = 'upload/video'
  if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

  # 获取视频类型, 视频大小
  video_type = file_obj.content_type
  video_size = file_obj.size

  # 重命名视频, md5(用户名+时间戳)
  file_name = file_obj.name
  file_name = file_name.split('.')
  file_name = hashlib.md5((user_data.username + str(time.time())).encode('utf-8')).hexdigest() + '.' + file_name[-1]

  # 保存视频到 ./upload/video
  try:
    with open(f'{upload_dir}/{file_name}', 'wb') as f:
      for chunk in file_obj.chunks():
        f.write(chunk)
  except Exception as e:
    print(e)
    return ResponseInfo.fail(500, '上传失败')

  # 保存上传记录
  upload_record = UploadRecord.objects.create(
    path=f'{upload_dir}/{file_name}',
    size=video_size,
    format=video_type,
    author=user_data
  )

  # 格式化输出 upload_record
  data = model_to_dict(upload_record)

  return ResponseInfo.success('上传成功', data)


# 观看视频
def get_video(request):
  """
  观看视频
  :param request:
  :return:
  """
  video_id = request.GET.get('id')
  print(video_id)
  if not video_id:
    return ResponseInfo.fail(400, '参数不全')

  video = UploadRecord.objects.filter(id=video_id).first()
  print(video)
  if not video:
    return ResponseInfo.fail(400, '视频不存在')

  return FileResponse(open(video.path, 'rb'))
