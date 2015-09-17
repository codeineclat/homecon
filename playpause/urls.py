from django.conf.urls import include, url
from playpause import views

urlpatterns = [
	url(r'^$',views.Playpause_Change, name='Playpause_Change'),
	url(r'^dashboard/$',views.Dashboard, name='Dashboard'),
	url(r'^graph/$',views.Graph, name='Graph'),
	url(r'^analytics/$',views.Analytics, name='Analytics'),
	url(r'^report/$',views.Report, name='Report'),
	url(r'^configre/$',views.Configure, name='Configure'),
	url(r'^machinelearning/$',views.Machine_Learning, name='Machine_Learning'),
	url(r'^errorlog/$',views.Error_Log, name='Error_Log'),
]