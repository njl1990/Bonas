from django.http import HttpResponse
from ci.models import NodeConnectInfo
from django.utils import timezone
from django.core import serializers

def index(request):
	list=NodeConnectInfo.objects.all()
	data = serializers.serialize("json", NodeConnectInfo.objects.all())
	return HttpResponse("NodeConnectInfo:"+data)
	
def dlgin(request):
	# get device login request
	device_id = request.GET['device_id']
	address = request.GET['address']
	
	# create ncd
	ncd=NodeConnectInfo()
	ncd.node_id=device_id
	ncd.node_address=address
	ncd.last_online_timestr=timezone.now()
	
	#save ncd
	ncd.save()
	
	return HttpResponse(0)

def dlgout(request):
	# get device login request
	device_id = request.GET['device_id']
	ncd = NodeConnectInfo.objects.filter(node_id=device_id)
	ncd.delete()
	return HttpResponse(0)