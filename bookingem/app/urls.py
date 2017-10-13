from django.conf.urls import url
from . import views

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^goods/$', views.goods, name='goods'),
    url(r'^goods/good/(?P<name>[\w\s#]+)/$', views.good, name='good'),
    url(r'^categories/category/(?P<name>[\w]+)/$', views.category, name='category'),
]