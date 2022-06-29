from django.contrib import messages
from django.shortcuts import render, redirect
from blog.models import Post
from django.shortcuts import get_object_or_404
from .forms import CommentForm

# Create your views here.
def comment(request, pk):
    post = get_object_or_404(Post,pk=pk)  # 根据pk查找post对象
    # print('\n\n\nrequest.POST:', request.POST)
    form = CommentForm(request.POST)  # 通过提交的POST数据生成表单对象

    if form.is_valid():
        comment = form.save(commit=False)   # 表单对象的save方法将生成对应的模型实例，commit表示是否将模型数据保存数据库
        comment.post = post   # 提交的POST数据中并没有post的数据
        comment.save()   # 最后保存到数据库

        # 消息被缓存在 cookie 中，然后我们在模板中获取显示即可。
        messages.add_message(request, messages.SUCCESS,'评论发表成功！',extra_tags='success')
        return redirect(post)  # 重定向一个模型时，将调用这个模型的get_absolute_url 方法
    # 如果没有重定向，说明表单有误，则渲染一个错误页面，展示错误详情
    messages.add_message(request,messages.ERROR,'评论失败！请修改表单中的错误后再重新提交。', extra_tags='danger')
    context = {
        'post': post,
        'form': form,
    }
    return render(request, r'comment\preview.html', context=context)



