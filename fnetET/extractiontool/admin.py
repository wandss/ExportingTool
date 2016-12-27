from django.contrib import admin
from extractiontool.models import *

class CmisServerAdmin(admin.ModelAdmin):
	list_display = ['server_name', 'server_address']

admin.site.register(CmisServer, CmisServerAdmin)
