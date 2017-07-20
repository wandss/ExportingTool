from django.shortcuts import render, HttpResponse
from django.views import generic
from extractiontool.fnet import Fnet


class DownloadView(generic.View):

    def get(self, request):
        context = {}
        username = request.session.get('username')
        passwd = request.session.get('passwd')
        server_uri = request.session.get('server_uri')
        repo = Fnet(server_uri, username, passwd)
        repo.getFnetClasses()
        context['repo_classes'] = repo.classes
        return render(request, 'download_content_list.html', context)

    def post(self, request):
        context = {}
        username = request.session.get('username')
        passwd = request.session.get('passwd')
        server_uri = request.session.get('server_uri')
        repo = Fnet(server_uri, username, passwd)
        if 'classe_id' in request.POST:
            context['repo_class'] = repo.getClass(request.POST.get('classe_id'))

        return render(request, 'download_content_list.html', context)
