from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import CmisServer

class ServerList(generic.ListView):
    model = CmisServer

class ServerCreate(generic.edit.CreateView):
    model = CmisServer
    fields = ['server_name', 'server_address']
    success_url = '/'

