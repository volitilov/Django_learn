from django.conf.urls import url

from .views import PostView

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^$', PostView.as_view(template_name='blog.html'), name='blog'),
]