from django.conf.urls import url

from .views import BlogListView, PostDetailView
from .views2 import PostCreate, PostEdit, PostDelete

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^categories/(?P<name>[\w\s]+)/$', 
        BlogListView.as_view(template_name='blog.html'), 
        name='blog'),
        
    url(r'^post/(?P<title>[\w\s]+)$', 
        PostDetailView.as_view(template_name='post.html'), 
        name='post'),
    
    url(r'^post/(?P<name>[\w\s]+)/add$', 
        PostCreate.as_view(template_name='post_add.html'), 
        name='post_add'),
    url(r'^post/(?P<title>[\w\s]+)/edit$', 
        PostEdit.as_view(template_name='post_edit.html'), 
        name='post_edit'),
    url(r'^post/(?P<title>[\w\s]+)/del$', 
        PostDelete.as_view(template_name='post_del.html'), 
        name='post_del'),
]