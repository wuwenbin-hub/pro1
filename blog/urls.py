from django.urls import path
from . import views

app_name = 'blog'  # 告诉程序，当前的url模块属于哪个应用，此次是blog应用  ---  试图函数命名空间

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archives, name='archives'),
    path('category/<int:pk>/', views.category, name='category'),
    path('tag/<int:pk>/', views.tag, name='tag')

]
