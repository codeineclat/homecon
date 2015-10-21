from django.shortcuts import render,HttpResponse,render_to_response
from django.http import JsonResponse
import datetime
import pytz
from accon.models import ACLog,ACAction,ACSucess,ACFail,ACErrorlog,ACDetails,ACStoreconfiginfo
from services.models import Pings, Recent_Request,Recent_App_Request
from django.utils.timezone import utc
from . import acconcontrol
from django.template import RequestContext
import json

def Last_Ping_Time_Diff(Time):
	now = datetime.datetime.utcnow().replace(tzinfo=utc)
	PingTime = int((now - Time).total_seconds())

	if(PingTime > 60):
		PingTime = int(PingTime /60)
		if(PingTime > 60):
			PingTime = int(PingTime / 60)
			if(PingTime > 24):
				PingTime = int(PingTime / 24)
				if(PingTime > 30):
					PingTime = int(PingTime / 30)
					if(PingTime > 12):
						PingTime = int(PingTime / 12)
						TimeString = str(PingTime) + " yrs "
					else:
						TimeString = str(PingTime) + " mnts "		
				else:
					TimeString = str(PingTime) + " days "	
			else:
				TimeString = str(PingTime) + " hrs "			
		else:
			TimeString = str(PingTime) + " min "		
	else:
		TimeString = str(PingTime) + " sec "

	return TimeString

def Get_Device_Info(sDeviceId,sValue,sSpeed):
	sDeviceId = sDeviceId[-1]
	
	if sValue == '00':
		svalue = 0
	elif sValue == '01':
		svalue = 1
	else:
		svalue = sSpeed 

	return sDeviceId,svalue	

def Accon_Change(request):
	if request.method == 'POST':
		
		sDeviceId = request.POST.getlist('sDeviceId')
		sValue    = request.POST.getlist('sValue')
		sSpeed    = request.POST.getlist('sSpeed')
		sAppID    = request.POST.getlist('sAppID')


		sDeviceId = str(sDeviceId)
		sDeviceId = sDeviceId[2:-2]
		
		sValue  = str(sValue)
		sAppID  = str(sAppID)
		sSpeed  = str(sSpeed)

		tz = pytz.timezone("Asia/Kolkata")
		time = (datetime.datetime.now(tz=tz))
		sSiliconid = "181E0BC8000E1440"

		sValue  = sValue[2:-2]		
		sAppID  = sAppID[2:-2]
		sSpeed  = sSpeed[2:-2]
		sSpeed = int(sSpeed)

		sId,sv = Get_Device_Info(sDeviceId,sValue,sSpeed)

		try:
			sDeviceInfo = ACDetails.objects.get(id =sId)
			sinfo = sDeviceInfo.device_info
			sDeviceInfo.current_value = sv
			sDeviceInfo.current_scale = sv * 10
			sDeviceInfo.save()

		except Exception as e:
			sinfo = ""
			sv = 0
			sErrorlog = ACErrorlog(error_at = time, error_name = str(e))
			sErrorlog.save()

		scale = sv * 10
		
		try:
			sConfigInfo = ACStoreconfiginfo.objects.latest('id')
			sXbee = sConfigInfo.xbee_number

		except Exception as e:
			sErrorlog = ACErrorlog(error_at = time, error_name = str(e))
			sErrorlog.save()

		try:
			sAcconDetail = ACDetails.objects.get(id =sId)
			sDeviceId   		= sAcconDetail.device_id
			sDevicePlace        = sAcconDetail.device_place
			sDeviceCurrentValue = sAcconDetail.current_value

		except Exception as e:
			sErrorlog = ACErrorlog(error_at = time, error_name = str(e))
			sErrorlog.save()

		try:
			sLog = ACLog.objects.latest('id')
			if (sLog.action_taken == 0):
				sFail = ACFail(fail_at = time,siliconid=sSiliconid,log_id=sLog.id)
				sFail.save()
		except Exception as e:
			sErrorlog = ACErrorlog(error_at = time, error_name = e)
			sErrorlog.save()

		sStringpacket = acconcontrol.Accon_Packet_Constractor(sAppID,sDeviceId,sDevicePlace,sDeviceCurrentValue,sXbee)

		sLogToDatabase = ACLog(log_at=time,log_deviceid=sDeviceId,log_value = sValue,
			log_speed = sSpeed,packet_str = sStringpacket,log_appid = sAppID,
			log_info_id=sId,log_info = sinfo,siliconid=sSiliconid)
		sLogToDatabase.save()

		sAppRequest = Recent_App_Request(app_id=sAppID,app_name="accon")
		sAppRequest.save()

		try:
			sAcconDetail = ACDetails.objects.get(id =sId)
			sDeviceName 		= sAcconDetail.device_name
			sDeviceInfo 		= sAcconDetail.device_info
			sDeviceId   		= sAcconDetail.device_id
			sDeviceImgOn 		= sAcconDetail.device_img_on
			sDeviceImgOff 		= sAcconDetail.device_img_off
			sDevicePlace        = sAcconDetail.device_place
			sDeviceCurrentValue = sAcconDetail.current_value
			sDeviceScale        = sAcconDetail.current_scale

		except Exception as e:
			sErrorlog = ACErrorlog(error_at = time, error_name = str(e))
			sErrorlog.save()
			sAcconDetail = ""
			sDeviceName  = ""
			sDeviceInfo  = ""
			sDeviceId    = ""
			sDeviceImgOn = ""
			sDeviceImgOff = ""
			sDevicePlace  = ""
			sDeviceCurrentValue = ""
			sDeviceScale = ""
		
		try:
			sAcconAction = ACAction.objects.latest('id')
			sAcconActionTime = sAcconAction.action_at
			sAcconActionTime = Last_Ping_Time_Diff(sAcconActionTime)

			sAcconActionInfo = (ACLog.objects.get(id = sAcconAction.log_id)).log_info
			sAcconActionValue = (ACLog.objects.get(id = sAcconAction.log_id)).log_speed

		except Exception as e:
			sErrorlog = ACErrorlog(error_at = time, error_name = str(e))
			sErrorlog.save()
			sAcconActionTime  =""
			sAcconActionInfo  =""
			sAcconActionValue =""

		try:
			sAcconSucess = ACSucess.objects.latest('id')
			sAcconSucessTime = sAcconSucess.sucess_at
			sAcconSucessTime = Last_Ping_Time_Diff(sAcconSucessTime)

			sAcconSucessInfo   = (ACLog.objects.get(id = sAcconSucess.log_id)).log_info
			sAcconSucessStatus = sAcconSucess.sucess_status

		except Exception as e:
			sErrorlog = ACErrorlog(error_at = time, error_name = str(e))
			sErrorlog.save()
			sAcconSucessTime   =""
			sAcconSucessInfo   =""
			sAcconSucessStatus =""

		try:
			sAcconFail = ACFail.objects.latest('id')
			sAcconFailTime = sAcconFail.fail_at
			sAcconFailTime = Last_Ping_Time_Diff(sAcconFailTime)

			sAcconFailInfo = (ACLog.objects.get(id = sAcconFail.log_id)).log_info
			sAcconFailValue = (ACLog.objects.get(id = sAcconFail.log_id)).log_speed

		except Exception as e:
			sErrorlog = ACErrorlog(error_at = time, error_name = str(e))
			sErrorlog.save()
			sAcconFailTime  =""
			sAcconFailInfo  =""
			sAcconFailValue =""


		sAcconDetail = {'devicename':sDeviceName,'deviceinfo':sDeviceInfo,'deviceid':sDeviceId,
		'deviceimgon':sDeviceImgOn,'deviceimgoff':sDeviceImgOff,'deviceplace':sDevicePlace,
		'devicecurrentvalue':sDeviceCurrentValue,'devicescale':sDeviceScale,
		'acconfailtime': sAcconFailTime,'acconfailinfo':sAcconFailInfo,'acconfailvalue':sAcconFailValue,
		'acconactiontime':sAcconActionTime,'acconactioninfo':sAcconActionInfo,'acconactionvalue':sAcconActionValue,
		'acconsucesstime':sAcconSucessTime,'acconsucessinfo':sAcconSucessInfo,'acconsucessstatus':sAcconSucessStatus,}

		return HttpResponse(json.dumps({'saccondetail':sAcconDetail}))

	try:
		sAcconDetail = ACDetails.objects.all()
	except Exception as e:
		sErrorlog = ACErrorlog(error_at = time, error_name = str(e))
		sErrorlog.save()
		sAcconDetail = ""

	return render(request,"accon/accon.html",{'sAcconDetail': sAcconDetail})

def Dashboard(request):
	
	return render(request,"accon/accon_dashboard.html")

def Report(request):
	test = "ok"
	return render(request,"accon/accon_report.html",{"test":test})

def Configure(request):
	test = "ok"
	return render(request,"accon/accon_configure.html",{"test":test})

def Graph(request):
	test = "ok"
	return render(request,"accon/accon_graph.html",{"test":test})

def Machine_Learning(request):
	test = "ok"
	return render(request,"accon/accon_machinelearning.html",{"test":test})

def Analytics(request):
	test = "ok"
	return render(request,"accon/accon_analytics.html",{"test":test})

def Error_Log(request):
	try:
		sErrorlog = Errorlog.objects.all()
	except:
		sErrorlog = "no error"
	return render(request,"accon/accon_errorlog.html",{"sErrorlog":sErrorlog})