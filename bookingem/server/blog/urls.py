from django.conf.urls import url

from .views import BlogListView, PostDetailView

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^categories/(?P<name>[\w\s]+)/$', 
        BlogListView.as_view(template_name='blog.html'), 
        name='blog'),
        
    url(r'^post/(?P<title>[\w\s]+)$', 
        PostDetailView.as_view(template_name='post.html'), 
        name='post'),
]