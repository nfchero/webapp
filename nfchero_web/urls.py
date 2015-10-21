from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from nfchero_web import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'nfchero_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
