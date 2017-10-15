from django.views.generic.list import ListView
from .models import Category, Good

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class GoodListView(ListView):
    paginate_by = 3
    goods = None

    def get(self, request, *args, **kwargs):
        self.goods = Good.objects.order_by('name')
        return super(GoodListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('id')
        context["goods"] = self.goods
        context['title'] = 'Goods'
        return context

    def get_queryset(self):
        return Good.objects.filter(category=self.cat).order_by("name")

