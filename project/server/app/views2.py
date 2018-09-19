from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from .models import Good, Category

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class GoodListView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        goods = Good.objects.order_by('name')
        paginator = Paginator(goods, 3)
        print(self.request)
        try:
            page_num = self.request.GET['page']
        except KeyError:
            page_num = 1

        try:
            context['goods'] = paginator.page(page_num)
            self.request.session['prev_page'] = self.request.get_full_path()
        except InvalidPage:
            context['goods'] = paginator.page(1)
            self.request.session['prev_page'] = 1
        context['title'] = 'Goods'
        context['categories'] = Category.objects.order_by('id')
        return context


class GoodDetailView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        try:
            good = Good.objects.get(name=kwargs['name'])
            context['good'] = good
            context['title'] = good.name
            context['categories'] = Category.objects.order_by('id')
            context['prev_page'] = self.request.session['prev_page']
        except Good.DoesNotExist:
            raise Http404
        return context



class CategoryListView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        try:
            category = Category.objects.get(name=kwargs['name'])
            if kwargs['name'] == 'Все':
                goods = Good.objects.all()
            else:
                goods = category.good_set.all()
            paginator = Paginator(goods, 1)
            try:
                page_num = self.request.GET['page']
            except KeyError:
                page_num = 1
            try:
                goods = paginator.page(page_num)
                self.request.session['prev_page'] = self.request.get_full_path()
            except InvalidPage:
                goods = paginator.page(1)
                self.request.session['prev_page'] = 1

            context['title'] = category.name
            context['category'] = category
            context['categories'] = Category.objects.order_by('id')
            context['goods'] = goods
        except Category.DoesNotExist:
            raise Http404
        return context

