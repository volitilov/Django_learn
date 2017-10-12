from django.conf.urls import url
from . import views

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^goods/(?:(?P<pk>\d+)/)?$', views.goods, name='goods'),
    url(r'^goods/good/(?P<id>\d+)/$', views.good, name='good'),
]