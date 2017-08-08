from django.conf.urls import url
from repo.views import DownloadView, BrowseRepoView

urlpatterns = [
    url(r'^content/$', DownloadView.as_view(), name='contents'),
    url(r'^browse/$', BrowseRepoView.as_view(), name='browse'),
]
