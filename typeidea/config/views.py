from django.shortcuts import render, HttpResponse
from blog.views import CommonViewMixin
from django.views.generic import ListView

from .models import Link


class LinkListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'
