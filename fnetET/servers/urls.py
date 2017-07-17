from django.conf.urls import url
from servers.views import ServerList

urlpatterns = [
    url(r'^$', ServerList.as_view()),
]
