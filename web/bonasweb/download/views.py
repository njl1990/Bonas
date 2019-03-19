from django.http import FileResponse  
def index(request):  
    file=open('./file/example.tar.gz','rb')  
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="example.tar.gz"'  
    return response