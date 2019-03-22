from django.db import models

class Project(models.Model):
	project_name = models.CharField(max_length=200)
	project_dscp = models.CharField(max_length=200)

class Chapter(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	chapter_name = models.CharField(max_length=200)
	chapter_dscp = models.CharField(max_length=200)
	total_value = models.IntegerField(default=0)
	current_value = models.IntegerField(default=0)