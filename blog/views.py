import re

import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

from blog.models import Post, Tag, Category


def index(request):
    post_list = Post.objects.all()
    return render(request,'blog/index.html', context={'post_list':post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # 系统定义的pk是关键
    # markdown.markdown方法将markdown文本解析成了 HTML 文本
    md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      TocExtension(slugify=slugify),
                                  ])
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', context={'post': post})



def archives(request,year,month):
    """
    根据创建年月查询文章列表
    """
    post_list = Post.objects.filter(
        created_time__year = year,
        created_time__month = month,
    )
    return render(request, "blog/index.html", context={"post_list":post_list})


def category(request, pk):
    """
    根据文章分类查询文章列表
    """
    cat = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(
        category = cat
    )
    return render(request,'blog/index.html', context={'post_list': post_list})

def category_count(request, pk):
    """
    根据文章分类查询文章列表
    """
    cat = get_object_or_404(Category, pk=pk)
    return len(cat)


def tag(request, pk):
    """
    根据文章分类查询文章列表
    """
    t = get_object_or_404(Tag,pk=pk)   # 查询pk=pk的标签对象
    post_list = Post.objects.filter(    # 根据标签对象查询文章对象
        tag=t
    )
    return render(request,'blog/index.html', context={'post_list':post_list})
