from django.contrib import admin
from blog.models import Post,Tag,Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']  # 列表页展示的字段
    fields = ['title', 'abstract', 'category', 'tag', 'body']  # 展开详情页后的显示字段

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)