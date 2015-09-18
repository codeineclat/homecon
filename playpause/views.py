from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import datetime
import pytz
from playpause.models import Log,Action,Sucess,Fail
from services.models import Pings, Recent_Request
from django.utils.timezone import utc
from . import playpausecontrol

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

def Playpause_Change(request):
	if request.method == 'POST':

		sPlaypauseValue = request.POST.getlist('sPlaypauseValue')
		sCommand        = request.POST.getlist('sCommand')
		sFunction       = request.POST.getlist('sFunction')
		sAppID          = request.POST.getlist('sAppID')

		sPlaypauseValue = str(sPlaypauseValue)
		sFunction       = str(sFunction)
		sCommand        = str(sCommand)
		sAppID          = str(sAppID)

		sFunction       = sFunction[2:-2]
		sPlaypauseValue = sPlaypauseValue[2:-2]
		sCommand        = sCommand[2:-2]
		sAppID          = sAppID[2:-2]

		tz = pytz.timezone("Asia/Kolkata")
		time = (datetime.datetime.now(tz=tz))
		sSiliconid = "181E0BC8000E1440"
		sStringpacket = playpausecontrol.Palypause_Packet_Constractor(sAppID,sCommand,sFunction)

		if sPlaypauseValue != "get_info":

			sLog = Log.objects.latest('id')
			if (sLog.action_taken == 0):
				sFail = Fail(fail_at = time,siliconid=sSiliconid,log_id=sLog.id)
				sFail.save()

			sLogToDatabase = Log(log_at=time,log_value=sPlaypauseValue,log_cmd = sCommand,
				log_function = sFunction,log_appid = sAppID,siliconid=sSiliconid,
				packet_str = sStringpacket)
		
			sLogToDatabase.save()

		sLastPing = Pings.objects.latest('id')
		sLog      = Log.objects.latest('id')
		sAction   = Action.objects.latest('id')
		sSucess   = Sucess.objects.latest('id')
		sFail     = Fail.objects.latest('id')

		PingTime       = sLastPing.sPingAt
		PingTime       = Last_Ping_Time_Diff(PingTime)

		CmdRequest     = sLog.log_value
		CmdRequestTime = sLog.log_at
		CmdRequestTime = Last_Ping_Time_Diff(CmdRequestTime)

		CmdActionTime  = sAction.action_at
		CmdActionTime  = Last_Ping_Time_Diff(CmdActionTime)

		CmdAction      = (Log.objects.get(id = sAction.log_id)).log_value

		CmdStatus      = sSucess.sucess_status
		CmdStatusTime  = sSucess.sucess_at
		CmdStatusTime  = Last_Ping_Time_Diff(CmdStatusTime)
		CmdCmd         = (Log.objects.get(id = sSucess.log_id)).log_value

		FailCmd        = (Log.objects.get(id = sFail.log_id)).log_value
		FailTime       = sFail.fail_at
		FailTime       = Last_Ping_Time_Diff(FailTime)

		sLastPingInfo = {'pingat':PingTime,'siliconid' :sLastPing.sSiliconID,
						'RSSI':99,'cmdrequest':CmdRequest,'cmdrequesttime':CmdRequestTime,
						'cmdaction':CmdAction,'cmdactiontime':CmdActionTime,'cmdstatus':CmdStatus,
						'cmdstatustime':CmdStatusTime,'cmdcmd':CmdCmd,'failcmd':FailCmd,
						'failtime':FailTime,}

	sLastPing = Pings.objects.latest('id')
	sLog      = Log.objects.latest('id')
	sAction   = Action.objects.latest('id')
	sSucess   = Sucess.objects.latest('id')
	sFail     = Fail.objects.latest('id')
	
	PingTime       = sLastPing.sPingAt
	PingTime       = Last_Ping_Time_Diff(PingTime)

	CmdRequest     = sLog.log_value
	CmdRequestTime = sLog.log_at
	CmdRequestTime = Last_Ping_Time_Diff(CmdRequestTime)

	CmdActionTime  = sAction.action_at
	CmdActionTime  = Last_Ping_Time_Diff(CmdActionTime)

	CmdAction      = (Log.objects.get(id = sAction.log_id)).log_value

	CmdStatus      = sSucess.sucess_status
	CmdStatusTime  = sSucess.sucess_at
	CmdStatusTime  = Last_Ping_Time_Diff(CmdStatusTime)
	CmdCmd         = (Log.objects.get(id = sSucess.log_id)).log_value

	FailCmd        = (Log.objects.get(id = sFail.log_id)).log_value
	FailTime       = sFail.fail_at
	FailTime       = Last_Ping_Time_Diff(FailTime)

	sLastPingInfo = {'pingat':PingTime,'siliconid' :sLastPing.sSiliconID,
					'RSSI':99,'cmdrequest':CmdRequest,'cmdrequesttime':CmdRequestTime,
					'cmdaction':CmdAction,'cmdactiontime':CmdActionTime,'cmdstatus':CmdStatus,
					'cmdstatustime':CmdStatusTime,'cmdcmd':CmdCmd,'failcmd':FailCmd,
					'failtime':FailTime,}

	return render(request,"playpause/playpause.html",{'sLastPingInfo': sLastPingInfo})

def Dashboard(request):
	
	return render(request,"playpause/playpause.html",{'sLastPingInfo': sLastPingInfo})

def Report(request):
	test = "ok"
	return render(request,"playpause/playpause_report.html",{"test":test})

def Configure(request):
	test = "ok"
	return render(request,"playpause/playpause_configure.html",{"test":test})

def Graph(request):
	test = "ok"
	return render(request,"playpause/playpause_graph.html",{"test":test})

def Machine_Learning(request):
	test = "ok"
	return render(request,"playpause/playpause_machinelearning.html",{"test":test})

def Analytics(request):
	test = "ok"
	return render(request,"playpause/playpause_analytics.html",{"test":test})

def Error_Log(request):
	test = "ok"
	return render(request,"playpause/playpause_errorlog.html",{"test":test})
