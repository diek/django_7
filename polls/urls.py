from django.conf.urls import patterns, url


from polls import views

#The next step is to point the root URLconf at the polls.urls module.
# In mysite/urls.py insert an include(),
urlpatterns = patterns('', url(r'^$', views.index, name='index'), )
