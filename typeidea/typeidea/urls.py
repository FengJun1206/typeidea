"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from blog.views import post_list, post_detail
from config.views import links

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='post_list'),    # 文章列表页，首页
    re_path(r'^post/(?P<post_id>\d+).html$', post_detail, name='post_detail'),       # 文章详情页
    re_path(r'^category/(?P<category_id>\d+).html$', post_list, name='categoty'),
    re_path(r'^tag(?P<tag_id>\d+).html$', post_list, name='tag'),
    path('links/', links, name='links'),      # 友链
]
