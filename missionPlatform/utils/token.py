# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： token.py
    @date：2024/8/18 上午11:24

"""
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


# 生成 token
def create_jwt_pair_for_user(user: User):
  refresh = RefreshToken.for_user(user)

  tokens = {"access": str(refresh.access_token), "refresh": str(refresh)}

  return tokens


# 刷新 token
def refresh_jwt_token(token: str):
  try:
    refresh = RefreshToken(token)
    access = str(refresh.access_token)
    return access
  except Exception as e:
    # Log the exception if needed
    # logger.error(f"Token refresh failed: {e}")
    return None


# 校验 token
def verify_jwt_token(token: str, refresh_token: str):
  try:
    data = JWTAuthentication().get_validated_token(token)
    user = JWTAuthentication().get_user(data)
    password = JWTAuthentication().get_user(data)
    print(user)
    print(password)
    print(data)

    print(refresh_jwt_token(refresh_token))

    return True
  # 如果 token 过期
  except Exception as e:
    # Log the exception if needed
    # logger.error(f"Token verification failed: {e}")
    return False
