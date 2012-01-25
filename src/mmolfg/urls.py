"""
URLConf for MMOLFG sites.
"""

from django.conf.urls.defaults import (
    include,
    patterns,
    url,
)

from mmolfg import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),
    (r'^accounts/', include('mmolfg.accounts.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='home'),
)
