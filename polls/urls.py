from django.conf.urls import patterns, url
from polls.views import archive 

urlpatterns = patterns('',
   # url(r'^$', views.index, name='index'),
    url(r'^$',archive),
)
