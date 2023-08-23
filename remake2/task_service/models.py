# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    # 标题
    title = models.CharField(max_length=100)

    # 详情
    description = models.TextField(null=True, blank=True)

    # 截止日期
    deadline = models.DateTimeField(null=True, blank=True)

    # 优先级
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')

    # 状态
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='not_started')
    # 依赖任务 (只有完成此任务后才能开始当前任务)
    depends_on = models.OneToOneField('self', null=True, blank=True, on_delete=models.SET_NULL,
                                      related_name='next_task')
    # 分配给
    assigned_to = models.ForeignKey(User, related_name='tasks_assigned', null=True, blank=True,
                                    on_delete=models.SET_NULL, to_field='id')  # 使用 id 作为实际值

    # 创建者
    created_by = models.ForeignKey(User, related_name='tasks_created', on_delete=models.CASCADE,
                                   to_field='id')  # 使用 id 作为实际值

    # 标签/类别
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title
    @property
    def assigned_to_name(self):
        if self.assigned_to:
            return self.assigned_to.username  # 返回分配给用户名
        return None

    @property
    def created_by_name(self):
        return self.created_by.username  # 返回创建者用户名

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()  # 包括文本和可能的表情符号
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.task}'
