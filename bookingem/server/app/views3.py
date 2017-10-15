from django.views.generic.base import ContextMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Category, Good

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class ContextData(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('id')
        return context


class GoodListView(ListView, ContextData):
    paginate_by = 3
    goods = None
    category = None

    def get(self, request, *args, **kwargs):
        self.category = Category.objects.get(name=self.kwargs['name'])
        if self.kwargs['name'] == 'Все':
            self.goods = Good.objects.all()
        else:
            self.goods = self.category.good_set.all()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category.name
        context['category'] = self.category
        context['goods'] = self.goods
        self.request.session['prev_page'] = self.request.get_full_path()
        return context

    def get_queryset(self):
        return self.goods


class GoodDetailView(DetailView, ContextData):
    model = Good
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Good'
        context['prev_page'] = self.request.session['prev_page']
        return context
