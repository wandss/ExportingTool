#encoding=utf-8

from django.shortcuts import render, HttpResponse, redirect
from django.template import RequestContext
from django.contrib.auth import logout
from fnet import Fnet, Conecta
from getContentWithIDAnyClass import GetDocuments
from extractiontool.models import *

def index(request):
	context = {}	
	if request.method == 'POST':

		if request.POST.get('server_name'):
			"""Acessed when creating or editing a server"""
			server_name = request.POST.get('server_name')
			server_address = request.POST.get('server_address')
			edit = request.POST.get('edit')
			if edit:				
				CmisServer.objects.filter(pk = edit).update(
					server_name=server_name,
					server_address=server_address)
				return redirect('/')
			CmisServer(server_name=server_name, 
				server_address=server_address).save()
			return redirect('/')

		if not request.POST.get('chosen_props'):
			"""Getting the Available Classes from a given server"""	
			if not request.session.keys():
				user = request.POST.get('username')
				passwd = request.POST.get('passwd')
				request.session['user'] = user
				request.session['passwd'] = passwd
			else:
				user = request.session['user']
				passwd = request.session['passwd']
		
			chosen_server = request.POST.get('available_servers')			
			server = CmisServer.objects.filter(server_name = chosen_server)	
			context['servers'] = server
			context['chosen_server'] = True					
			fnet = Fnet(server[0].server_address, user, passwd)

			if type(fnet.rep) == type(str()):
				context['errors'] = {'Error' : fnet.rep}
				return render(request, "index.html", context)

			if server and not request.POST.has_key('selected_class'):				
				available_classes = fnet.getFnetClasses()								
				context['available_classes'] = available_classes

				return render(request, "index.html", context)	

			myclass = request.POST.get('selected_class')					
			fnet_class = fnet.getClass(myclass)
			context['available_classes'] = [fnet_class]
			properties = fnet.removeSystemProperties(fnet_class.properties)
			context['properties'] = properties
			context['available_classes']
			return render(request, "index.html", context)	
		
		user = request.session['user']
		passwd = request.session['passwd']	
		chosen_server = request.POST.get('available_servers')			
		server = CmisServer.objects.filter(server_name = chosen_server)
		fnet = Fnet(server[0].server_address, user, passwd)
		chosen_properties = request.POST.get('chosen_props').split(',')
		doc_class = request.POST.get('selected_class')
		fnet_ids = [ids.strip('\r') for ids in request.POST.get('fnet_ids').split('\n')]		
		saveDocs = GetDocuments(chosen_properties, fnet.rep, fnet_ids, doc_class)
				
		if saveDocs.errors:
			context['errors'] = saveDocs.errors

	if not request.session.keys():
		context['no_user'] = True
	servers = CmisServer.objects.all()
	if not servers or request.GET.has_key('newserver'):
		if servers:
			context['saved_servers'] = servers
		return render(request, "index.html", context)

	context['servers'] = servers	
	return render(request, "index.html", context)


def remove(request):	
	CmisServer.objects.filter(pk=request.GET.keys()[0]).delete()	
	return redirect('/')

def appinfo(request):	
	page = request.GET.keys()[0]
	print page
	context = {page : True,
				'text': True}
	return render(request, 'index.html', context)

def out(request):
	logout(request)
	return redirect('/')