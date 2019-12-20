from django.shortcuts import render

import pysnooper
from .models import Post, Category, Tag
from config.models import SideBar


@pysnooper.snoop()
def post_list(request, category_id=None, tag_id=None):
    """文章列表页"""
    tag, category = None, None
    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_categoty(category_id)
    else:
        post_list = Post.latest_posts()
        print('post_list', post_list)

    context = {
        'tag': tag,
        'categoty': category,
        'post_list': post_list,
        'sidebar_list': SideBar.get_all()
    }

    context.update(Category.get_navs())

    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    """文章详情页"""
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post,
        'sidebar_list': SideBar.get_all()
    }
    return render(request, 'blog/detail.html', locals())
