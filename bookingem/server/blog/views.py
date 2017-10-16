from django.views.generic.dates import ArchiveIndexView

from .models import Post

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class PostView(ArchiveIndexView):
    model = Post
    date_field = 'pub_date'
