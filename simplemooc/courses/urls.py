from django.conf.urls import url

from simplemooc.courses.views import index, details

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^(?P<pk>\d+)/$', details, name='details'),
    url(r'^(?P<slug>[\w,-]+)/$', details, name='details'),

]
