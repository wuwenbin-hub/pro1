from django import template

from comments.forms import CommentForm

register = template.Library()

@register.inclusion_tag(r'comment\inclusions\_form.html',takes_context=True)
def show_comments_form(context, post, form=None):
    if form is None:
        form = CommentForm()

    # 如果表单已存在，就复用已有的评论表单实例
    return {
        'form': form,
        'post': post,
    }

@register.inclusion_tag(r'comment\inclusions\_comment.html',takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_list':comment_list,
        'comment_count': comment_count,
    }
