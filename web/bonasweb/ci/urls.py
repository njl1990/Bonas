from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('dlgin/',views.dlgin,name='dlgin'),
	path('dlgout/',views.dlgout,name='dlgout'),
	
]
