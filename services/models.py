from django.db import models
import datetime
import pytz

def call_time_now():
	sTimeZone = pytz.timezone("Asia/Kolkata")
	sTime = (datetime.datetime.now(tz=sTimeZone))
	return sTime


class Pings(models.Model):
	sPingAt    = models.DateTimeField()
	sPacket    = models.TextField()
	sSiliconID = models.CharField(max_length=20)

	def __str__(self):
		return str(self.sSiliconID) 

class Recent_Request(models.Model):
	request_at         = models.DateTimeField(auto_now=True,blank=True)
	request_packet     = models.TextField(default="")
	request_siliconid  = models.CharField(max_length=16)
	served_at          = models.DateTimeField(blank=True)
	sucess_at          = models.DateTimeField(blank=True)
	request_status     = models.BooleanField(default=0)

	def __str__(self):
		return str(self.request_appid)

class Recent_App_Request(models.Model):
	app_id   = models.CharField(default="",max_length=20)
	app_name = models.CharField(default="",max_length=20)
	def __str__(self):
		return str(self.app_name)

class Serrorlog(models.Model):
	error_name   = models.CharField(default="",max_length=1000)
	error_at   = models.DateTimeField(default=None,blank=True)
	
	def __str__(self):
		return str(self.error_name)