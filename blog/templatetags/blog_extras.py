from django import template
from ..models import Post, Category, Tag

# 用于注册模板标签和过滤器的对象
register = template.Library()

# register.inclusion_tag装饰器：
#                      将show_recent_posts_tag函数注册为inclusion_tag类型的模板标签

@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts_tag(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num], #返回查询结果的前5个文章
    }

@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        "date_list":Post.objects.dates('created_time','month', order='DESC'),   # dates(属性，种类，顺序) 查询得到日期列表   ---属性，查询的是哪个属性的日期列表； ---种类，年月日； ---顺序，升降
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }

@register.inclusion_tag('blog/inclusions/_tag.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list':Tag.objects.all(),
    }