from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from userservice.models import CustomUser


class Command(BaseCommand):
    help = 'Create user groups and permissions'

    def handle(self, *args, **kwargs):
        # 定义权限codenames
        permissions_codenames = ['view_CustomUser', 'add_CustomUser', 'change_CustomUser', 'delete_CustomUser']

        # 获取CustomUser的ContentType
        content_type = ContentType.objects.get_for_model(CustomUser)

        # 创建或获取未登录用户组，并分配查看权限
        guest_group, _ = Group.objects.get_or_create(name='Guest')
        guest_group.permissions.add(Permission.objects.get(codename='view_CustomUser', content_type=content_type))

        # 创建或获取普通登录用户组，并分配查看、添加和修改权限
        user_group, _ = Group.objects.get_or_create(name='User')
        user_group.permissions.set(
            Permission.objects.filter(codename__in=permissions_codenames[:-1], content_type=content_type))

        # 创建或获取管理员用户组，并分配所有权限
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        admin_group.permissions.set(
            Permission.objects.filter(codename__in=permissions_codenames, content_type=content_type))

        self.stdout.write(self.style.SUCCESS('Successfully created groups and permissions'))
