from django.conf.urls import url
from . import views
from .views2 import GoodListView, GoodDetailView, CategoryListView

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^goods/$',
        GoodListView.as_view(template_name='goods.html'), 
        name='goods'),
    url(r'^goods/(?P<name>[\w\s#]+)/$', 
        GoodDetailView.as_view(template_name='good.html'), 
        name='good'),
    url(r'^goods/category/(?P<name>[\w]+)/$', 
        CategoryListView.as_view(template_name='category.html'), 
        name='category'),
]