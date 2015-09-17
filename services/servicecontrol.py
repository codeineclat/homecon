def Service_Packet_Constractor(packet_str,sSiliconid):
	sStringPacket = '!'
	sStringPacket = sStringPacket + sSiliconid
	sStringPacket = sStringPacket + "*01$"
	sStringPacket = sStringPacket + packet_str
	sStringPacket = sStringPacket + '000000000000000000000000000000000000000000000000000000'
	sStringPacket = sStringPacket + '000000000000000000000000000000000000000000000000000000'
	sStringPacket = sStringPacket + '000000000000000000000000000000000000000000000000000000'
	sStringPacket = sStringPacket + '00000000000000000000000000000000000000000000000000#'
	
	return sStringPacket