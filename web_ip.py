import socket
print("                   WEBSITE IP ADDRESS FINDER.\n                 /////////////////////////////")
def ip():
	try:
		web_name=input("enter website name--->")
		url=input("enter website url ---> ")
		print(f'ip address of {web_name} is {socket.gethostbyname(url)}\n\n')
	except:
		print("plz enter valid url\n\n")
ip()
print("\t\tThanx for choosing us")