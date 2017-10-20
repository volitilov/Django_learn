from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView, ProcessFormView
)
from django.core.urlresolvers import reverse

from .views3 import ContextData
from .models import Good, Category

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


class GoodCreate(CreateView, ContextData):
    model = Good
    fields = ['name', 'description', 'category', 'in_stock']
    template_name = 'good_add.html'

    def get(self, request, *args, **kwargs):
        if self.kwargs['name'] != None:
            self.initial['category'] = Category.objects.get(name=self.kwargs['name'])
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('category', 
            kwargs={'name': Category.objects.get(name=self.kwargs['name'])})
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(name=self.kwargs['name'])
        context['title'] = context['category'].name
        context['prev_page'] = self.request.session['prev_page']
        return context


class GoodUpdate(UpdateView, ContextData):
    model = Good
    fields = ['name', 'description', 'category', 'in_stock']
    template_name = 'good_edit.html'
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('category', 
            kwargs={'name': Good.objects.get(name=self.kwargs['name']).category})
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prev_page'] = self.request.session['prev_page']
        return context


class GoodDelete(DeleteView, ContextData):
    model = Good
    template_name = 'good_del.html'
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def post(self, request, *args, **kwargs):
        self.success_url = reverse('category', 
            kwargs={'name': 'Все'})
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['good'] = Good.objects.get(name=self.kwargs['name'])
        return context

