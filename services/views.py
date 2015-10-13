from django.shortcuts import render, HttpResponse
from services.models import Pings,Recent_Request
from django.utils import timezone
import datetime
import pytz
from playpause.models import Log,Action,Sucess
from . import servicecontrol




def Ping_Packet(request):
	print (request)
	sPingPacket = request.GET.get('pkt', '')
	sTimeZone = pytz.timezone("Asia/Kolkata")
	sTime = (datetime.datetime.now())
	sSiliconid = sPingPacket[1:17]
	sDObject = Pings(sPacket=sPingPacket, sSiliconID=sSiliconid,sPingAt=sTime)
	sDObject.save()

	if(sSiliconid == "181E0BC8000E1440"):
		try:
			sLastLog = Log.objects.latest('id')
		
			if(sLastLog.action_taken == 0):
				sValue = sLastLog.packet_str
				sLastLog.action_taken = '1'
				sAction = Action(log_id=sLastLog.id,action_at=sTime,siliconid=sLastLog.siliconid)
			
				sAction.save()
				sLastLog.save()

				sStringPacket = servicecontrol.Service_Packet_Constractor(sValue,sSiliconid)
				s = Recent_Request(request_at=sTime,request_siliconid=sSiliconid,
					request_packet=sStringPacket,served_at=sTime,sucess_at=sTime)
				s.save()
				return HttpResponse(sStringPacket)

			else:
				sStringPacket = servicecontrol.Service_No_Packet_Constractor('181E0BC8000E1440')
				return HttpResponse(sStringPacket)
				
		except Exception as e:
				sErrorlog = Serrorlog(error_at = time, error_name = e)
				sErrorlog.save()
				sStringPacket = servicecontrol.Service_No_Packet_Constractor('181E0BC8000E1440')
				return HttpResponse(sStringPacket)