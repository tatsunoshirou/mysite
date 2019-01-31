from django.db import models

# Create your models here.
from django.utils.timezone import now


class Post(models.Model):
    name = models.CharField('名前', max_length=32, blank=False)
    title = models.CharField('題名', max_length=32, blank=False)
    message = models.TextField('投稿内容', max_length=145)
    created_at = models.DateTimeField(default=now)

    class Meta:
        db_table = 'post'
        verbose_name = verbose_name_plural = '投稿'
