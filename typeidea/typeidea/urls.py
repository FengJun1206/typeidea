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
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.conf import settings

from blog.views import (
    IndexView, CategoryView, TagView, PostDetailView,
    SearchView, AuthorView)
from comment.views import CommentView

from config.views import (LinkListView)
from .custom_site import custom_site

from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap

import xadmin
from .autocomplete import CategoryAutoComplete, TagAutoComplete

urlpatterns = [
    re_path('^$', IndexView.as_view(), name='index'),  # 文章列表页，首页
    re_path(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    re_path(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),  # 作者页面
    re_path(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'), # 文章详情页
    re_path(r'^links/$', LinkListView.as_view(), name='links'),  # 友链
    re_path(r'^search/$', SearchView.as_view(), name='search'),     # 搜索
    re_path(r'^comment/$', CommentView.as_view(), name='comment'),  # 评论

    re_path(r'^rss|feed$', LatestPostFeed(), name='rss'),
    re_path(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),

    # 自动补全
    re_path(r'^category-autocomplete/$', CategoryAutoComplete.as_view(), name='category-autocomplete'),
    re_path(r'^tag-autocomplete/$', TagAutoComplete.as_view(), name='tag-autocomplete'),

    # path('admin/', admin.site.urls),
    re_path(r'^super_admin/', admin.site.urls, name='super-admin'),
    # re_path(r'^admin/', custom_site.urls, name='admin'),
    re_path(r'^admin/', xadmin.site.urls, name='xadmin'),

    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# from blog.views import post_list, post_detail
# from config.views import links
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', post_list, name='post_list'),    # 文章列表页，首页
#     re_path(r'^post/(?P<post_id>\d+).html$', post_detail, name='post_detail'),       # 文章详情页
#     re_path(r'^category/(?P<category_id>\d+).html$', post_list, name='categoty'),
#     re_path(r'^tag(?P<tag_id>\d+).html$', post_list, name='tag'),
#     path('links/', links, name='links'),      # 友链
# ]
