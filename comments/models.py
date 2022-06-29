from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField('姓名', max_length=50)
    email = models.EmailField('邮箱')
    url = models.URLField('网址', blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now())  # default:创建时添加  save函数：保存到数据库时添加
    post = models.ForeignKey('blog.Post', verbose_name='文章', on_delete=models.CASCADE)  # 外键，品论的文章

    class Meta:
        verbose_name = '评论'  # 后台中模型的显示名称
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}:{}'.format(self.name, self.text[:20])

