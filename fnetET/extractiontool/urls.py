from django.conf.urls import include, url

urlpatterns = [    
    url(r'^$','extractiontool.views.index'),     
    url(r'^remove/$','extractiontool.views.remove'),
    url(r'out/$','extractiontool.views.out'),
    url(r'appinfo/$','extractiontool.views.appinfo'),
    ]