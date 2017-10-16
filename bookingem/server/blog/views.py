from django.views.generic.base import ContextMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post, BlogCategory

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class ContextData(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.order_by('id')
        return context


class BlogListView(ListView, ContextData):
    paginate_by = 3
    posts = None
    category = None

    def get(self, request, *args, **kwargs):
        self.category = BlogCategory.objects.get(name=self.kwargs['name'])
        if self.kwargs['name'] == 'Все':
            self.posts = Post.objects.all()
        else:
            self.posts = self.category.post_set.all()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category.name
        context['category'] = self.category
        context['posts'] = self.posts
        self.request.session['prev_page'] = self.request.get_full_path()
        return context

    def get_queryset(self):
        return self.posts



class PostDetailView(DetailView, ContextData):
    model = Post
    slug_field = 'title'
    slug_url_kwarg = 'title'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Post'
        context['prev_page'] = self.request.session['prev_page']
        return context
