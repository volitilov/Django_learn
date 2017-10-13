from django.shortcuts import render
from django.http import (
    request, HttpResponse, Http404
)
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Category, Good

# :::::::::::::::::::::::::::::::::::::::::::::

def index(request):
   return render(request, 'index.html')


def goods(request):
    goods = Good.objects.all().order_by('name')
    try:
        page_num = request.GET['page']
    except KeyError:
        page_num = 1
    pag = Paginator(goods, 5)
    goods = pag.page(page_num)
    data = {
        'title': 'Goods',
        'categories': Category.objects.all().order_by('id'),
        'goods': goods
    }
    return render(request, 'goods.html', data)


def good(request, name):
    try:
        good = Good.objects.get(name=name)
        data = {
            'good': good,
            'title': good.name,
            'categories': Category.objects.all().order_by('id')
        }
    except Good.DoesNotExist:
        raise Http404
    return render(request, 'good.html', data)



def category(request, name):
    try:
        category = Category.objects.get(name=name)
        goods = category.good_set.all()
        data = {
            'title': category.name,
            'category': category,
            'categories': Category.objects.all().order_by('id'),
            'goods': goods.order_by('id')
        }
    except Category.DoesNotExist:
        raise Http404
    return render(request, 'category.html', data)
