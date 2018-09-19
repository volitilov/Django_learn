from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import redirect
from .models import Good, Category
from .forms import GoodFiltersForm

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class GoodFilters(TemplateView):
    form = None

    def get(self, request):
        self.form = GoodFiltersForm()
        return super().get(request)

    def post(self, request):
        self.form = GoodFiltersForm(request.POST)
        if self.form.is_valid():
            data = {
                'category': self.form.cleaned_data['category'].name,
                'in_stock': self.form.cleaned_data['in_stock']
            }
            self.request.session['results'] = data
            return redirect('results')
        else:
            return super().post(request)
    
    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = self.form
        return context


class ResultsListView(ListView):
    results = None
    category = None
    goods = None
    in_stock = None

    def get(self, request):
        self.results = self.request.session['results']
        self.category = self.results['category']
        self.in_stock = self.results['in_stock']
        if self.category == 'Все':
            self.goods = Good.objects.filter(in_stock=self.in_stock).order_by('name')
        else:
            self.goods = Good.objects.filter(category__name=self.category, 
                    in_stock=self.in_stock).order_by('name')
        return super().get(request)

    def get_context_data(self):
        context = super().get_context_data()
        context['category'] = self.category
        context['categories'] = Category.objects.order_by('id')
        self.request.session['prev_page'] = self.request.get_full_path()
        return context

    def get_queryset(self):
        return self.goods