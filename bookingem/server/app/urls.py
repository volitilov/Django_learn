from django.conf.urls import url
from .views3 import (
    GoodListView, GoodDetailView
)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^(?P<name>[\w\s#]+)/$', 
        GoodDetailView.as_view(template_name='good.html'), 
        name='good'),

    url(r'^category/(?P<name>[\w]+)/$', 
        GoodListView.as_view(template_name='category.html'), 
        name='category'),
]