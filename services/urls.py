from django.conf.urls import include, url

urlpatterns = [
	url(r'^$','services.views.Ping_Packet'),
]