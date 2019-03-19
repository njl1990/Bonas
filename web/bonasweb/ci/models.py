from django.db import models


# Create your models here.
class NodeConnectInfo(models.Model):

	# node identification field
    node_id = models.CharField(max_length=200)
    # last online time
    last_online_timestr = models.DateTimeField('date published')
    # connection information
    node_address = models.CharField(max_length=200)