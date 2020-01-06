from django.db import models

from blog.models import Post


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    target = models.CharField(max_length=100, verbose_name='评论目标')  # 用于存储文章 url，从而获取文章 id，而后判断用户
    # target = models.ForeignKey(Post, verbose_name='评论目标', on_delete=models.CASCADE)
    content = models.CharField(max_length=2000, verbose_name='评论内容')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    website = models.URLField(verbose_name='网站')
    email = models.EmailField(verbose_name='邮箱')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '评论'

    @classmethod
    def get_by_target(cls, target):
        """某篇文章的有效评论"""
        return cls.objects.filter(target=target, status=cls.STATUS_NORMAL)
