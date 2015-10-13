from django.shortcuts import render,HttpResponse,render_to_response
from django.http import JsonResponse
import datetime
import pytz
from accon.models import ACLog,ACAction,ACSucess,ACFail,ACErrorlog,ACDetails
from services.models import Pings, Recent_Request
from django.utils.timezone import utc
#from . import acconcontrol
from django.template import RequestContext


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


def Accon_Change(request):
	if request.method == 'POST':

		sAcconValue = request.POST.getlist('sAcconValue')
		sCommand        = request.POST.getlist('sCommand')
		sFunction       = request.POST.getlist('sFunction')
		sAppID          = request.POST.getlist('sAppID')

		sAcconValue = str(sAcconValue)
		sAcconValue = sAcconValue[2:-2]
		

		sFunction       = str(sFunction)
		sAppID          = str(sAppID)

		tz = pytz.timezone("Asia/Kolkata")
		time = (datetime.datetime.now(tz=tz))
	
		sFunction       = sFunction[2:-2]		
		sAppID          = sAppID[2:-2]
		sLastPingInfo = "test"


	try:
		sAcconDetail = ACDetails.objects.all()
	except Exception as e:
		sErrorlog = Errorlog(error_at = time, error_name = str(e))
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