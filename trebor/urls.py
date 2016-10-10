from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from trebor import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'trebor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^detail/$', views.Detail.as_view(), name='detail'),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
