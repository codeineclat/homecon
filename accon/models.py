from django.db import models
from django.contrib.auth.models import User

class ACDetails(models.Model):
	device_name    = models.CharField(max_length=20, default='0')
	device_info    = models.CharField(default="",max_length=256)
	device_id      = models.IntegerField(null=True,default=0)
	device_img_on  = models.CharField(default="",max_length=256)
	device_img_off = models.CharField(default="",max_length=256)
	device_place   = models.IntegerField(null=True,default=0)
	current_value  = models.IntegerField(null=True,default=0)
	current_scale  = models.IntegerField(null=True,default=0)
	
	def __str__(self):
		return str(self.device_info)

class ACLog(models.Model):
	user           = models.ForeignKey(User,null=True,blank=True)
	log_at         = models.DateTimeField(default=None,blank=True)
	log_deviceid   = models.TextField(default="")
	log_value      = models.CharField(max_length=20, default='0')
	log_speed      = models.IntegerField(null=True,default=0)
	log_appid      = models.CharField(max_length=20, default='0')
	log_info       = models.CharField(default="",max_length=256)
	log_info_id    = models.IntegerField(null=True,default=0)
	siliconid      = models.CharField(default="",max_length=20)
	action_taken   = models.BooleanField(default=0)
	packet_str     = models.CharField(default="",max_length=256)
	
	def __str__(self):
		return str(self.packet_str)

class ACAction(models.Model):
	log_id         = models.IntegerField(null=True)
	siliconid      = models.CharField(default="",max_length=20)
	action_at      = models.DateTimeField(default=None,blank=True)

	def __str__(self):
		return str(self.log_id)

class ACSucess(models.Model):
	log_id         = models.IntegerField(null=True)
	siliconid      = models.CharField(default="",max_length=20)
	sucess_status  = models.BooleanField(default=0)
	sucess_at      = models.DateTimeField(default=None,blank=True)
	response_str   = models.CharField(default="",max_length=256)

	def __str__(self):
		return str(self.log_id)

class ACFail(models.Model):
	log_id         = models.IntegerField(null=True)
	siliconid      = models.CharField(default="",max_length=20)
	fail_at        = models.DateTimeField(default=None,blank=True)

	def __str__(self):
		return str(self.log_id)


class ACErrorlog(models.Model):
	error_name   = models.CharField(default="",max_length=1000)
	error_at   = models.DateTimeField(default=None,blank=True)
	
	def __str__(self):
		return str(self.error_name)

class ACStoreconfiginfo(models.Model):
	xbee_name = models.CharField(default="",max_length=256)
	xbee_number = models.CharField(default="",max_length=256)

	def __str__(self):
		return str(xbee_name)