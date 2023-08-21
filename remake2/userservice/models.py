from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class CustomUser(AbstractBaseUser):
    # 添加自定义字段
    USERNAME_FIELD = 'username'



