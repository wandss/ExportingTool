from django.conf.urls import include, url
from extractiontool.views import IndexView

urlpatterns = [    
    url(r'^$',IndexView.as_view(), name='index'),       
    #url(r'^$','extractiontool.views.index'),     
    #url(r'^remove/$','extractiontool.views.remove'),
    #url(r'out/$','extractiontool.views.out'),
    #url(r'appinfo/$','extractiontool.views.appinfo'),
    ]
