from django.conf.urls import url
from repo.views import DownloadContentView

urlpatterns = [
    url(r'^content/$', DownloadContentView.as_view(), name='contents'),
]
