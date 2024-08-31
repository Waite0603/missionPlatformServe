import json

from django.core.paginator import Paginator

from article.models import Article
from missionPlatform.decorators import post_only, login_required, get_only
from missionPlatform.utils.response import ResponseInfo
from missionPlatform.utils.token import get_user_info
from missionPlatform.utils.tools import model_to_dict


# 新增文章
@post_only
@login_required
def add_article(request):
  user_data = get_user_info(request)

  try:
    data = json.loads(request.body)
  except json.JSONDecodeError:
    return ResponseInfo.fail(400, 'Invalid JSON')

  title = data.get('title')
  english_title = data.get('englishTitle')
  content = data.get('content')
  author = user_data

  if not all([title, english_title, content]):
    return ResponseInfo.fail(400, '参数不全')

  cover = data.get('cover')

  if not cover:
    cover = 'cover_default.jpg'

  # 保存文章
  article = Article.objects.create(
    title=title,
    english_title=english_title,
    content=content,
    cover=cover,
    author=author
  )

  # 返回作者名字
  article_dict = model_to_dict(article)
  article_dict['author'] = article.author.username

  return ResponseInfo.success('新增文章成功', article_dict)


# 获取单篇文章
@get_only
def get_article(request):
  article_id = request.GET.get('id')

  if not article_id:
    return ResponseInfo.fail(400, '参数不全')

  article = Article.objects.filter(id=article_id).first()

  if not article:
    return ResponseInfo.fail(404, '文章不存在')

  # 返回作者名字
  article_dict = model_to_dict(article)
  article_dict['author'] = article.author.username

  return ResponseInfo.success('获取文章成功', article_dict)


# 修改文章
@post_only
@login_required
def update_article(request):
  user_data = get_user_info(request)

  try:
    data = json.loads(request.body)
  except json.JSONDecodeError:
    return ResponseInfo.fail(400, 'Invalid JSON')

  article_id = data.get('id')
  title = data.get('title')
  english_title = data.get('englishTitle')
  content = data.get('content')
  author = user_data

  if not all([article_id, title, english_title, content]):
    return ResponseInfo.fail(400, '参数不全')

  cover = data.get('cover')

  if not cover:
    cover = 'cover_default.jpg'

  # 更新文章
  article = Article.objects.filter(id=article_id).first()

  if not article:
    return ResponseInfo.fail(404, '文章不存在')

  article.title = title
  article.english_title = english_title
  article.content = content
  article.cover = cover
  article.author = author

  article.save()

  # 返回作者名字
  article_dict = model_to_dict(article)
  article_dict['author'] = article.author.username
  article_dict['author_avatar'] = article.author.avatar

  return ResponseInfo.success('修改文章成功', article_dict)


# 获取文章列表
@get_only
def get_article_list(request):
  # 获取页码, 默认第一页
  page = request.GET.get('page', 1)

  # 获取每页数量, 默认 10 条
  page_size = request.GET.get('pageSize', 10)

  # 获取文章列表
  article_list = Article.objects.filter(status=1).order_by('-create_time')

  # 分页
  paginator = Paginator(article_list, page_size)

  # 获取当前页数据
  page_data = paginator.page(page)

  # 格式化输出
  data = []
  for article in page_data:
    article_dict = model_to_dict(article)
    article_dict['author'] = article.author.username
    data.append(article_dict)

  res_dict = {
    'total': paginator.count,
    'page': page,
    'pageSize': page_size,
    'data': data
  }

  return ResponseInfo.success('获取文章列表成功', res_dict)


# 删除文章
@post_only
@login_required
def delete_article(request):
  try:
    data = json.loads(request.body)
  except json.JSONDecodeError:
    return ResponseInfo.fail(400, 'Invalid JSON')

  article_id = data.get('id')

  if not article_id:
    return ResponseInfo.fail(400, '参数不全')

  # 删除文章
  try:
    article = Article.objects.filter(id=article_id).first().delete()
  except AttributeError:
    return ResponseInfo.fail(404, '文章不存在')

  return ResponseInfo.success('删除文章成功')


# 推荐文章
@get_only
def recommend_article(request):
  article_id = request.GET.get('id')

  if not article_id:
    return ResponseInfo.fail(400, '参数不全')
  article_list = Article.objects.all().order_by('-create_time')[:5]

  data = []
  for article in article_list:
    if article.id == int(article_id):
      continue
    article_dict = model_to_dict(article)
    article_dict['author'] = article.author.username
    data.append(article_dict)

  return ResponseInfo.success('获取推荐文章成功', data[:3])
