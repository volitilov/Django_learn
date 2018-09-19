from django.shortcuts import render
from django.http import (
    request, HttpResponse, Http404
)
from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage

from .models import Category, Good

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def goods(request):
    goods = Good.objects.order_by('name')
    paginator = Paginator(goods, 3)
    try:
        page_num = request.GET['page']
    except KeyError:
        page_num = 1
    try:
        goods = paginator.page(page_num)
    except InvalidPage:
        goods = paginator.page(1)
    data = {
        'title': 'Goods',
        'categories': Category.objects.order_by('id'),
        'goods': goods
    }
    return render(request, 'goods.html', data)


def good(request, name):
    try:
        good = Good.objects.get(name=name)
        data = {
            'good': good,
            'title': good.name,
            'categories': Category.objects.order_by('id'),
            'prev_page': request.session['prev_page']
        }
    except Good.DoesNotExist:
        raise Http404
    return render(request, 'good.html', data)



def category(request, name):
    try:
        category = Category.objects.get(name=name)
        if name == 'Все':
            goods = Good.objects.all()
        else:
            goods = category.good_set.all()
        paginator = Paginator(goods, 1)
        try:
            page_num = request.GET['page']
        except KeyError:
            page_num = 1
        try:
            goods = paginator.page(page_num)
            request.session['prev_page'] = page_num
        except InvalidPage:
            goods = paginator.page(1)
            request.session['prev_page'] = 1
        data = {
            'title': category.name,
            'category': category,
            'categories': Category.objects.order_by('id'),
            'goods': goods
        }
    except Category.DoesNotExist:
        raise Http404
    return render(request, 'category.html', data)


