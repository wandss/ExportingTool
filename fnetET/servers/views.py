#encoding: utf-8
from django.shortcuts import render, redirect
from django.views import generic
from .models import CmisServer

class ServerList(generic.ListView):
    model = CmisServer

class ServerCreate(generic.edit.CreateView):
    model = CmisServer
    fields = ['server_name', 'server_address']
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ServerCreate, self).get_context_data()
        context['servers'] = CmisServer.objects.all()
        return context

class ServerUpdate(generic.edit.UpdateView):
    model = CmisServer
    fields = ['server_name', 'server_address']
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ServerUpdate, self).get_context_data()
        context['servers'] = CmisServer.objects.all()
        return context

class ServerDelete(generic.edit.DeleteView):
    model = CmisServer
    success_url = '/'
    template_name = 'servers/confirm_delete.html'

    def post(self, request, **kwargs):
        if 'cancel' in request.POST:
            return redirect('/')

        return super(ServerDelete, self).post(request, kwargs)

