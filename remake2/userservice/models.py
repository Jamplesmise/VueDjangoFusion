# from django.db import models
# # Create your models here.
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#
#
# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=100, unique=True)
#     # add your custom fields here
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'username'
#
#     def get_by_natural_key(self, username):
#         return self.get(username=username)
#
#     # add other necessary methods
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
#
#
#
#
