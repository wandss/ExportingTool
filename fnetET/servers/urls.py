from django.conf.urls import url
from servers.views import ServerList, ServerCreate, ServerUpdate, ServerDelete

urlpatterns = [
    url(r'^$', ServerList.as_view()),
    url(r'^new/$', ServerCreate.as_view(),name='new_server'),
    url(r'^(?P<pk>[0-9]+)/update/$',ServerUpdate.as_view(), name='update_server'),       
    url(r'^(?P<pk>[0-9]+)/delete/$',ServerDelete.as_view(), name='delete_server'),       
]
