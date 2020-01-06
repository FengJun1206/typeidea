from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post, Category, Tag
from config.models import SideBar


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all()
        })
        context.update(Category.get_navs())
        return context


class IndexView(CommonViewMixin, ListView):
    """首页"""
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })

        return context

    def get_queryset(self):
        """重写queryset，根据分类进行过滤"""
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })
        return context

    def get_queryset(self):
        """ 重写querset，根据标签过滤 """
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id=tag_id)


class PostDetailView(CommonViewMixin, DetailView):
    """文章详情"""
    queryset = Post.latest_posts()
    print('>>>>>>>>>>>>>>>>>>>>', queryset)
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


class SearchView(IndexView):
    """搜索"""
    def get_context_data(self, **kwargs):
        """获取渲染到模板中的所有上下文"""
        print(self.request.GET.get('keyword', ''))
        context = super().get_context_data()
        context.update({
            'keyword': self.request.GET.get('keyword', '')
        })
        return context

    def get_queryset(self):
        """获取数据"""
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))


class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)

# @pysnooper.snoop()
# def post_list(request, category_id=None, tag_id=None):
#     """文章列表页"""
#     tag, category = None, None
#     if tag_id:
#         post_list, tag = Post.get_by_tag(tag_id)
#     elif category_id:
#         post_list, category = Post.get_by_categoty(category_id)
#     else:
#         post_list = Post.latest_posts()
#         print('post_list', post_list)
#
#     context = {
#         'tag': tag,
#         'categoty': category,
#         'post_list': post_list,
#         'sidebar_list': SideBar.get_all()
#     }
#
#     context.update(Category.get_navs())
#
#     return render(request, 'blog/list.html', context=context)


# def post_detail(request, post_id=None):
#     """文章详情页"""
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
#
#     context = {
#         'post': post,
#         'sidebar_list': SideBar.get_all()
#     }
#     return render(request, 'blog/detail.html', locals())
