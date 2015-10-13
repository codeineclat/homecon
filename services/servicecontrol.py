def Service_Packet_Constractor(packet_str,sSiliconid):
	sStringPacket = '!'
	sStringPacket = sStringPacket + sSiliconid
	sStringPacket = sStringPacket + "*01$"
	sStringPacket = sStringPacket + packet_str
	sStringPacket = sStringPacket + '000000000000000000000000000000000000000000000000000000'
	sStringPacket = sStringPacket + '000000000000000000000000000000000000000000000000000000'
	sStringPacket = sStringPacket + '000000000000000000000000000000000000000000000000000000'
	sStringPacket = sStringPacket + '00000000000000000000000000000000#'
	
	return sStringPacket


def Service_No_Packet_Constractor(sSiliconid):
	sStringPacket = '!'
	sStringPacket = sStringPacket + sSiliconid
	sStringPacket = sStringPacket + "*FD$"
	sStringPacket = sStringPacket + '0000000000000000000000'
	sStringPacket = sStringPacket + '000000000000000000000000000000000000000000000000000000'
	sStringPacket = sStringPacket + '000000000000000000000000000000000000000000000000000000'
	sStringPacket = sStringPacket + '000000000000000000000000000000000000000000000000000000'
	sStringPacket = sStringPacket + '00000000000000000000000000000000000000000000000000#'
	
	return sStringPacket