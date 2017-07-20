from django.conf.urls import url
from repo.views import DownloadView

urlpatterns = [
    url(r'^content/$', DownloadView.as_view(), name='contents'),
]
