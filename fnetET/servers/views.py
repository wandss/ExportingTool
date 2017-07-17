from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import CmisServer

class ServerList(ListView):
    model = CmisServer

