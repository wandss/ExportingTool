from django.contrib import admin
from .models import CmisServer

class CmisServerAdmin(admin.ModelAdmin):
    list_display = ['server_name', 'server_address','date_creation']

admin.site.register(CmisServer, CmisServerAdmin)    
