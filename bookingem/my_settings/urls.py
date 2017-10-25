from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView
from server.app.views5 import GoodFilters

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::

urlpatterns = [
    url(r'^$', GoodFilters.as_view(template_name='index.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^goods/', include('server.app.urls')),
    url(r'^blog/', include('server.blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
