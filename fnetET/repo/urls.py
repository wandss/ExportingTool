from django.conf.urls import url
from repo.views import repo_class

urlpatterns = [
    url(r'^content/$', repo_class, name='contents'),
]
