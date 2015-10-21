from random import randrange
import datetime

def Accon_Packet_Constractor(sAppID,sDeviceId,sDevicePlace,sDeviceCurrentValue,sXbee):
	
	uiCodeID = randrange(0,99)
	if(uiCodeID < 9):
		uiCodeID = '0' + str(uiCodeID)
	else:
		uiCodeID = str(uiCodeID)
	
	if(sDeviceCurrentValue < 9):
		sDeviceCurrentValue = '0' + str(sDeviceCurrentValue)
	else:
		sDeviceCurrentValue = str(sDeviceCurrentValue)

	sStringPacket = '*'
	sStringPacket = sStringPacket + sAppID + '$'
	sStringPacket = sStringPacket + "*" + sXbee + "$"
	sStringPacket = sStringPacket + "*05$"
	sStringPacket = sStringPacket + '*05'
	sStringPacket = sStringPacket + '0' + str(sDeviceId) + '0'+ str(sDevicePlace)+ sDeviceCurrentValue + uiCodeID + '$'
	
	return sStringPacket

