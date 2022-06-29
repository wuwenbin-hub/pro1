import django
import markdown
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import strip_tags
# Create your models here.
from django.urls import reverse  # 域名解析函数
from django.utils import timezone
from django.shortcuts import  get_object_or_404

class Category(models.Model):
    """
    blog的分类的模型
    """
    name = models.CharField('分类名', max_length=100)  # 分类名，字符类型的属性必须指明长度

    def __str__(self):   # 配置查询结果时显示的数据
        return self.name

    def get_count(self):
        """
        返回当前分类下的文章数量
        """
        posts = Post.objects.filter(category=self)
        return len(posts)

    class Meta:
        verbose_name = '分类'  # 数据模型在admin中的显示名字
        verbose_name_plural = '分类'  # 复数时数据模型在admin中的显示名字


class Tag(models.Model):
    """
    blog的标签的模型
    """
    name = models.CharField('标签名', max_length=100)  # 标签名
    def __str__(self):
        return self.name

    def get_count(self):
        return len(Post.objects.filter(tag=self))

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Post(models.Model):
    """
    博客数据模型
    """
    title = models.CharField('标题', max_length=70)  # 文章标题  出现过的错误：设置primary_key=True导致没有Post类没有自定义的pk
    body = models.TextField('正文')      # 文章正文，数据量太大用textfield
    created_time = models.DateTimeField('创建时间', default=timezone.now())    # 创建时间 datetimefield类型数据
    modified_time = models.DateTimeField('修改时间')    # 最后修改时间
    abstract = models.CharField('摘要',max_length=500, blank=True)   # 摘要 blank=True表示可以为空

    """
    category表示文章的分类，文章与分类属于一对多的关系，即一篇文章只能有一个分类，而一个分类可以包含多篇文章。
    此时分类对于文章来说是唯一的，分类就是文章的外键（相反却不行），表明一篇文章必须有且只有一个分类。
    on_delete=models.CASCADE为级联删除，表明当外键被删除后，当前对象也要被删除（属于该分类的所有文章都被删除）。
    """
    category = models.ForeignKey(Category, verbose_name='分类',on_delete=models.CASCADE)

    """
        tag表示文章的标签，文章与标签属于多对多的关系，即一篇文章可以有任意多个标签，而一个标签也可以包含多篇文章。
        标签属性不是必须的，所以blank=True
        """
    tag = models.ManyToManyField(Tag, verbose_name='标签',blank=True)

    """
    User来自系统定义的模型
    """
    author = models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        # markdown渲染对象
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        # md.covert()用于将markdown转换为html,strip_tags用于去掉html的标签，然后取前50个字符为摘要。
        # 注意：self.body本身默认是用markdown语法写的
        self.abstract = strip_tags(md.convert(self.body))[:50]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})   # 解析试图函数detail的URL，参数pk其值为self.pk

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_time']


