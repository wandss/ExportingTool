#encoding: utf-8
from django.shortcuts import render, HttpResponse
from django.views import generic
from extractiontool.fnet import Fnet
from extractiontool.getRepositoryContents import GetDocuments



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
        repo.getFnetClasses()

        if 'classe_id' in request.POST:
            doc_class = repo.getClass(request.POST.get('classe_id'))
            properties = repo.removeSystemProperties(doc_class.properties)
            context['repo_class'] = doc_class
            context['class_props'] = properties

        if 'search_by' in request.POST:
            doc_class = request.POST.get('class_id')
            compose_doc_name = request.POST.get('compose_doc_name').split(',')
            object_ids = request.POST.get('object_ids').split('\n')
            search_by = request.POST.get('search_by')
            contents = GetDocuments(doc_class, object_ids, search_by,
                                    compose_doc_name, repo.rep)
            contents.getContentWithQuery()
            context['warning'] = contents.checkCompletion()
            context['result_ok'] = contents.found_docs

        return render(request, 'download_content_list.html', context)

    """
    TODO:
        Criar lista com documentos localizados
        Ao fim retornar os numeros dos documentos lacalizados e documentos nao 
        localizados.
        Remover valores vazios da lista
        Adicionar mensagem de conclusão após finalizado downloads.
        Criar lista com os documentos localizados
        Criar mensagens de erro e bloco try
        Add object_id in class props list
        Add blank value as first item to class names list

        Testar serializar dados da classe. Isso permitirá que
        que, após escolhida a classe pelo usuário, não seja necessário uma nova
        conexão ao repositório.
        contudo, deverá ser criado uma classe com um método para ordenar as
        propriedades
    """
