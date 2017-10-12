from django.shortcuts import render
from django.http import request, HttpResponse
from django.shortcuts import render

from .models import Category, Good

# :::::::::::::::::::::::::::::::::::::::::::::

def index(request):
    return HttpResponse('Hello my name xxx')


def goods(request, pk):
    if pk == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk=pk)
    goods = Good.objects.filter(category=cat).order_by('name')
    s = 'Категория: ' + cat.name + '<br><br>'
    for good in goods:
        s = s + '(' + str(good.pk) + ')' + good.name + '<br>'
    return HttpResponse(s)


def good(request, id):
    good = Good.objects.get(pk=id)
    s = good.name + '<br><br>' + good.category.name + '<br><br>' + good.description
    if not good.in_stock:
        s = s + '<br><br>' + '- нет в наличии -'
    return HttpResponse(s)