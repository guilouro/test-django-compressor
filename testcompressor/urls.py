from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testcompressor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'testcompressor.core.views.index', name='core_index'),
    url(r'^admin/', include(admin.site.urls)),
)
