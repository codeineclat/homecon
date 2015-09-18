from django.db import models
from django.contrib.auth.models import User

class Log(models.Model):
	user           = models.ForeignKey(User,null=True,blank=True)
	log_at         = models.DateTimeField(default=None,blank=True)
	log_value      = models.TextField(default="")
	log_cmd        = models.CharField(max_length=20, default='0')
	log_function   = models.CharField(max_length=20, default='0')
	log_appid      = models.CharField(max_length=20, default='0')
	siliconid      = models.CharField(default="",max_length=20)
	action_taken   = models.BooleanField(default=0)
	packet_str     = models.CharField(default="",max_length=256)
	
	def __str__(self):
		return str(self.packet_str)

class Action(models.Model):
	log_id         = models.IntegerField(null=True)
	siliconid      = models.CharField(default="",max_length=20)
	action_at      = models.DateTimeField(default=None,blank=True)

	def __str__(self):
		return str(self.log_id)

class Sucess(models.Model):
	log_id         = models.IntegerField(null=True)
	siliconid      = models.CharField(default="",max_length=20)
	sucess_status  = models.BooleanField(default=0)
	sucess_at      = models.DateTimeField(default=None,blank=True)
	response_str   = models.CharField(default="",max_length=256)

	def __str__(self):
		return str(self.log_id)

class Fail(models.Model):
	log_id         = models.IntegerField(null=True)
	siliconid      = models.CharField(default="",max_length=20)
	fail_at        = models.DateTimeField(default=None,blank=True)

	def __str__(self):
		return str(self.log_id)



