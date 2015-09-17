from django.shortcuts import render, HttpResponse
from services.models import Pings,Recent_Request
from django.utils import timezone
import datetime
import pytz
from playpause.models import Log
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
		sLastLog = Log.objects.latest('id')
		sValue = sLastLog.packet_str
		sStringPacket = servicecontrol.Service_Packet_Constractor(sValue,sSiliconid)
		s = Recent_Request(request_at=sTime,request_siliconid=sSiliconid,
			request_packet=sStringPacket,served_at=sTime,sucess_at=sTime)
		s.save()
	return HttpResponse(sStringPacket)
