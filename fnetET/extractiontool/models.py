from django.db import models
from django.utils import timezone

class CmisServer(models.Model):
	server_name = models.CharField(max_length=50)
	server_address = models.CharField(max_length=100)
	date_creation = models.DateField(default = timezone.now)

	def __unicode__(self):
		return self.server_name

	class Meta:
		db_table = 'CmisServer'

