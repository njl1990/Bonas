from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from process.models import Project,Chapter
from django.template import loader

class IndexPageModel(Project):
	process=0

def index(request):
	indexPageModelList = []
	projectList =  Project.objects.all()
	for project in projectList:
		chapterList =  Chapter.objects.filter(project_id=project.id)
		total_sum = 0
		current_sum = 0
		percent=0
		for chapter in chapterList:
			total_sum = total_sum+chapter.total_value
			current_sum = current_sum+chapter.current_value
			percent = 100*current_sum/total_sum
		indexPageModel=IndexPageModel()
		indexPageModel.pk=project.pk
		indexPageModel.project_name=project.project_name
		indexPageModel.project_dscp=project.project_dscp
		indexPageModel.process=round(percent,1)
		indexPageModelList.append(indexPageModel);
	context = {'projectList': indexPageModelList}
	return render(request, 'index.html', context)

def getProject(request):
	projectList =  serializers.serialize("json", Project.objects.all())
	return HttpResponse(projectList)
	
def getAllChapterByProjectId(request,project_id):
	project = Project.objects.get(id=project_id)
	chapterList=Chapter.objects.filter(project_id=project_id)
	# count total percent
	total_sum=0
	current_sum=0
	for chapter in chapterList:
		total_sum = total_sum+chapter.total_value
		current_sum = current_sum+chapter.current_value
	total_percent = round(100*(current_sum/total_sum),1)
	context = {'project':project,'chapterList': chapterList,'total_percent':total_percent}
	return render(request, 'project.html', context)

def getChapterById(request,chapter_id):
	chapter = Chapter.objects.get(id=chapter_id)
	project = Project.objects.get(id=chapter.project_id)
	context = {'chapter':chapter,'project':project}
	return render(request, 'chapter.html', context)

def rollbackProcess(request,chapter_id):
	chapter=Chapter.objects.get(id=chapter_id)
	if(chapter.current_value<=0):
		return HttpResponse(0)
	chapter.current_value=chapter.current_value-1
	percent = round(100*(chapter.current_value/chapter.total_value))
	chapter.save()
	return HttpResponse(percent)

def finishProcess(request,chapter_id):
	chapter=Chapter.objects.get(id=chapter_id)
	chapter.current_value=chapter.total_value
	chapter.save()
	return HttpResponse("100")

def addProcess(request,chapter_id):
	chapter=Chapter.objects.get(id=chapter_id)
	if(chapter.current_value>=chapter.total_value):
		return HttpResponse(100)
	chapter.current_value=chapter.current_value+1
	percent = round(100*(chapter.current_value/chapter.total_value))
	chapter.save()
	return HttpResponse(percent)