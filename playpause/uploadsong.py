import os

path = os.getcwd()
path = path + "/" + "songlist.txt"

with open (path, "r") as myfile:
    data=myfile.read()

StringIndex = 0
index = 0
ToatalChar = len(data)
while(ToatalChar > 0):
	string = ""
	while(data[index] != '\n'):
		string = string + data[index]
		index = index + 1
	print (string)
	sSong = Songs(name=string)
	sSong.save()
	print ("\n\n")
	index = index + 1
	ToatalChar = ToatalChar - 1

