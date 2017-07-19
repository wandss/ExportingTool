from django.conf.urls import url
from servers.views import ServerList, ServerCreate

urlpatterns = [
    url(r'^$', ServerList.as_view()),
    url(r'^new/$', ServerCreate.as_view(),name='new_server'),
]
