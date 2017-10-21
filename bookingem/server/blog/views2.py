from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from .models import Post, BlogCategory
from .forms import PostForm

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class PostCreate(TemplateView):
    form = None
    category = None

    def get(self, request, **kwargs):
        self.category = BlogCategory.objects.get(name=self.kwargs['name'])
        self.form = PostForm(initial={
            'category': self.category})
        return super().get(request, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form = PostForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return redirect(self.request.session['prev_page'])
        else:
            return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['prev_page'] = self.request.session['prev_page']
        return context



class PostEdit(TemplateView):
    form = None
    category = None
    post = None

    def get(self, request, **kwargs):
        self.post = Post.objects.get(title=self.kwargs['title'])
        self.category = self.post.category
        self.form = PostForm(instance=self.post)
        return super().get(request, **kwargs)

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(title=self.kwargs['title'])
        self.form = PostForm(request.POST, instance=post)
        if self.form.is_valid():
            self.form.save()
            return redirect(self.request.session['prev_page'])
        else:
            return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['prev_page'] = self.request.session['prev_page']
        context['categories'] = BlogCategory.objects.order_by('id')
        return context



class PostDelete(TemplateView):
    def post(self, request, **kwargs):
        Post.objects.get(title=self.kwargs['title']).delete()
        return redirect(self.request.session['prev_page'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prev_page'] = self.request.session['prev_page']
        context['categories'] = BlogCategory.objects.order_by('id')
        return context
