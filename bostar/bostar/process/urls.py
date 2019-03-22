from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('getProject', views.getProject, name='getProject'),
	path('<int:project_id>/getAllChapterByProjectId', views.getAllChapterByProjectId, name='getAllChapterByProjectId'),
	path('<int:chapter_id>/getChapterById', views.getChapterById, name='getChapterById'),
]