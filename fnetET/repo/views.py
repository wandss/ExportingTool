from django.shortcuts import render, HttpResponse
from django.views import generic
from extractiontool.fnet import Fnet


def repo_class(request):
    context = {}
    username = request.session.get('username')
    passwd = request.session.get('passwd')
    server_uri = request.session.get('server_uri')
    repo = Fnet(server_uri, username, passwd)
    repo.getFnetClasses()
    if request.method == 'GET':
        context['repo_classes'] = repo.classes

    if request.method == 'POST':
        if 'classe_id' in request.POST:
            context['repo_class'] = repo.getClass(request.POST.get('classe_id'))

        import pdb;pdb.set_trace()
    return render(request, 'download_content_list.html', context)
