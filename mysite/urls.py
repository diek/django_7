from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # After we added namespace we had to adjust polls/index to
    # include the namespace as well
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
)
