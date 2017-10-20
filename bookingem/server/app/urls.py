from django.conf.urls import url
from .views3 import (
    GoodListView, GoodDetailView
)
from .views4 import (
    GoodCreate, GoodUpdate, GoodDelete
)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^(?P<name>[\s\w\.,#]+)/$', 
        GoodDetailView.as_view(template_name='good.html'), 
        name='good'),

    url(r'^category/(?P<name>[\w]+)/$', 
        GoodListView.as_view(template_name='category.html'), 
        name='category'),

    url(r'^category/(?P<name>[\w]+)/add$', GoodCreate.as_view(), name='good_add'),
    url(r'^(?P<name>[\w\s\.,#]+)/edit$', GoodUpdate.as_view(), name='good_edit'),
    url(r'^(?P<name>[\w\s\.,#]+)/delete$', GoodDelete.as_view(), name='good_del'),
]