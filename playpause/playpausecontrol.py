from . import MP3_Constant
from random import randrange
import datetime

def Palypause_Packet_Constractor(sAppID,sCommand,sFunction):
	
	uiCodeID = randrange(0,99)
	if(uiCodeID < 9):
		uiCodeID = '0' + str(uiCodeID)
	else:
		uiCodeID = str(uiCodeID)

	sStringPacket = '*'
	sStringPacket = sStringPacket + sAppID + '$'
	sStringPacket = sStringPacket + "*05$"
	sStringPacket = sStringPacket + '*05' + sFunction + sCommand + uiCodeID + '$'

	return sStringPacket

