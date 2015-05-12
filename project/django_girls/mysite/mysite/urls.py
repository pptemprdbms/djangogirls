from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 	url(r'^$', 'trips.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/(?P<id>\d+)/$', 'trips.views.post_detail',name='post_detail'),
)
