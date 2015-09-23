from django.shortcuts import render,HttpResponse,render_to_response
from django.http import JsonResponse
import datetime
import pytz
from playpause.models import Log,Action,Sucess,Fail,Uploadfile,Songs,Errorlog,Getlastsong
from services.models import Pings, Recent_Request
from playpause.forms  import UploadFileForm 
from django.utils.timezone import utc
from . import playpausecontrol
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


def Songlist_string_Converter(sCommand):
	if(sCommand < 15):
		string = "000" + str(hex(sCommand))[2:]
	elif(sCommand < 256):
		string = "00" + str(hex(sCommand))[2:]
	elif(sCommand < 4095):
		string = "0" + str(hex(sCommand))[2:]
	else:
		string = str(hex(sCommand))[2:]

	return string

def Playpause_Change(request):
	if request.method == 'POST':

		sPlaypauseValue = request.POST.getlist('sPlaypauseValue')
		sCommand        = request.POST.getlist('sCommand')
		sFunction       = request.POST.getlist('sFunction')
		sAppID          = request.POST.getlist('sAppID')

		sPlaypauseValue = str(sPlaypauseValue)
		sPlaypauseValue = sPlaypauseValue[2:-2]
		

		sFunction       = str(sFunction)
		sAppID          = str(sAppID)

		tz = pytz.timezone("Asia/Kolkata")
		time = (datetime.datetime.now(tz=tz))

		if(sPlaypauseValue[0] == "'" and sPlaypauseValue[1] == 's'):
			sCommand = str(sCommand)
			sCommand = int(sCommand[2:-2])
			sCommand = Songlist_string_Converter(sCommand)

			sID = int(sPlaypauseValue[7:])
			sLastSong = Songs.objects.get(id =sID)
			slastsongstore = Getlastsong(song_name = sLastSong.name,song_id=sLastSong.id)
			slastsongstore.save()
			slog_song = sLastSong.name
			slog_song_id=sLastSong.id

		elif(sPlaypauseValue[0] == "f" and sPlaypauseValue[1] == 'm'):
			sCommand = str(sCommand)
			sCommand = sCommand[2:-2]
			try:
				sLog = Log.objects.latest('id')
				slastsongstore = Getlastsong(song_name = sLog.log_song,song_id=sLog.log_song_id)
				slastsongstore.save()
			except Exception as e:
				sErrorlog = Errorlog(error_at = time, error_name = e)

			slog_song   = "FM " + sPlaypauseValue
			slog_song_id= 0

		elif(sPlaypauseValue[0] == "m" and sPlaypauseValue[1] == 'p'):
			sCommand = str(sCommand)
			sCommand = sCommand[2:-2]
			try:
				sGetlastSong = Getlastsong.objects.latest('id')
				if(sPlaypauseValue == "mp3_prev"):
					if(sGetlastSong.song_id > 1):
						slog_song_id = (sGetlastSong.song_id - 1)
						sLastSong    = Songs.objects.get(id =slog_song_id)
						slog_song    = sLastSong.name
						slog_song_id = sLastSong.id

					else:
						slog_song_id= sGetlastSong.song_id
						sLastSong = Songs.objects.get(id =slog_song_id)
						slog_song = sLastSong.name
						slog_song_id=sLastSong.id
					slastsongstore = Getlastsong(song_name = sLastSong.name,song_id=sLastSong.id)
					
				elif(sPlaypauseValue == "mp3_next"):
					maxsong = Songs.objects.latest('id')
					if(sGetlastSong.song_id < maxsong.id):
						slog_song_id= (sGetlastSong.song_id + 1)
						sLastSong = Songs.objects.get(id =slog_song_id)
						slog_song = sLastSong.name
						slog_song_id=sLastSong.id
					else:
						slog_song_id= sGetlastSong.song_id
						sLastSong = Songs.objects.get(id =slog_song_id)
						slog_song = sLastSong.name
						slog_song_id=sLastSong.id

					slastsongstore = Getlastsong(song_name = sLastSong.name,song_id=sLastSong.id)

				else:
					slog_song_id = sGetlastSong.song_id
					sLastSong    = Songs.objects.get(id =slog_song_id)
					slog_song    = sLastSong.name
					slog_song_id = sLastSong.id
				
			except Exception as e:
				sErrorlog = Errorlog(error_at = time, error_name = e)
				slog_song   = "error" 
				slog_song_id= 0

				

		else:
			sCommand = str(sCommand)
			sCommand = sCommand[2:-2]
			slog_song   = "none" 
			slog_song_id= 0
			
		sFunction       = sFunction[2:-2]		
		sAppID          = sAppID[2:-2]
		
		sSiliconid = "181E0BC8000E1440"
		sStringpacket = playpausecontrol.Palypause_Packet_Constractor(sAppID,sCommand,sFunction)

		if sPlaypauseValue != "get_info":

			try:
				sLog = Log.objects.latest('id')
				if (sLog.action_taken == 0):
					sFail = Fail(fail_at = time,siliconid=sSiliconid,log_id=sLog.id)
					sFail.save()
			except Exception as e:
				sErrorlog = Errorlog(error_at = time, error_name = e)

			sLogToDatabase = Log(log_at=time,log_value=sPlaypauseValue,log_cmd = sCommand,
				log_function = sFunction,log_appid = sAppID,siliconid=sSiliconid,
				packet_str = sStringpacket,log_song = slog_song,log_song_id=slog_song_id)
			print (sLogToDatabase.log_song)
			sLogToDatabase.save()

		sLastPing = Pings.objects.latest('id')
		sLog      = Log.objects.latest('id')
		sAction   = Action.objects.latest('id')
		sSucess   = Sucess.objects.latest('id')
		sFail     = Fail.objects.latest('id')

		PingTime       = sLastPing.sPingAt
		PingTime       = Last_Ping_Time_Diff(PingTime)

		CmdRequest     = sLog.log_value
		
		if(CmdRequest[0] == "'" and CmdRequest[1] == "s"):
			print (CmdRequest)
			sID = int(CmdRequest[7:])
			sLastSong = Songs.objects.get(id =sID)
			print (sLastSong)

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

		try:
			sLastSong = sLastSong.name
		except Exception as e:
			print (e)
			sLastSong = "no song selected...."

		sLastPingInfo = {'pingat':PingTime,'siliconid' :sLastPing.sSiliconID,
						'RSSI':99,'cmdrequest':CmdRequest,'cmdrequesttime':CmdRequestTime,
						'cmdaction':CmdAction,'cmdactiontime':CmdActionTime,'cmdstatus':CmdStatus,
						'cmdstatustime':CmdStatusTime,'cmdcmd':CmdCmd,'failcmd':FailCmd,
						'failtime':FailTime,'lastsong':sLastSong,}

	sLastPing = Pings.objects.latest('id')
	sLog      = Log.objects.latest('id')
	sAction   = Action.objects.latest('id')
	sSucess   = Sucess.objects.latest('id')
	sFail     = Fail.objects.latest('id')

	PingTime       = sLastPing.sPingAt
	PingTime       = Last_Ping_Time_Diff(PingTime)

	CmdRequest     = sLog.log_value

	if(CmdRequest[0] == "'" and CmdRequest[1] == "s"):
			sID = int(CmdRequest[7:])
			sLastSong = Songs.objects.get(id =sID)

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

	sSonglist      = Songs.objects.all()

	try:
		sLastSong = sLastSong.name
	except Exception as e:
		sLastSong = "no song selected..."
	

	sLastPingInfo = {'pingat':PingTime,'siliconid' :sLastPing.sSiliconID,
					'RSSI':99,'cmdrequest':CmdRequest,'cmdrequesttime':CmdRequestTime,
					'cmdaction':CmdAction,'cmdactiontime':CmdActionTime,'cmdstatus':CmdStatus,
					'cmdstatustime':CmdStatusTime,'cmdcmd':CmdCmd,'failcmd':FailCmd,
					'failtime':FailTime,'lastsong':sLastSong,}
	
	return render(request,"playpause/playpause.html",{'sLastPingInfo': sLastPingInfo,'sSonglist': sSonglist})

def Dashboard(request):
	
	return render(request,"playpause/playpause_dashboard.html")

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


def Uploadfileview(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		print (form)
		if form.is_valid():
			new_file = UploadFile(file = request.FILES['file'])
			new_file.save()
			return HttpResponse("sucess")
		else:
			form = UploadFileForm()

	data = {'form': form}
	return render_to_response('playpause/uploadfile.html', data, context_instance=RequestContext(request))
	