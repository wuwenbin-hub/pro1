from django import forms
from .models import Comment
"""
通过调用这个表单类的一些方法和属性，django 将自动为我们创建常规的表单代码，而不是在html文件中编辑，类似于ORM系统。
"""

"""
那么怎么展现一个表单呢？django 会根据表单类的定义自动生成表单的 HTML 代码，
我们要做的就是实例化这个表单类，然后将表单的实例传给模板，让 django 的模板引擎来渲染这个表单。
"""
class CommentForm(forms.ModelForm):
    # 表单类，继承自forms
    # forms.ModelForm表单有对应的数据模型
    # forms.Form表单可以没有对应的数据模型

    class Meta:   # 元类，用于指定父类的功能或标准
        model = Comment   # 表单对应的数据模型
        fields = ['name', 'email', 'url', 'text']   # 用于展示的字段