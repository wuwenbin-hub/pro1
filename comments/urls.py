from django.urls import path
from . import views

app_name = 'comments'  # 告诉程序，当前的url模块属于哪个应用，此次是blog应用  ---  试图函数命名空间

urlpatterns = [
    path('comment/<int:pk>', views.comment, name='comment')
]
