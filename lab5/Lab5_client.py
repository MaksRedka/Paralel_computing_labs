import socket, threading, time

shutdown = False
join = False

def receving (name, sock):#function for receiving and printing information from server
	while not shutdown:
		try:#trying to exequte code below
			while True:
				data, addr = sock.recvfrom(1024) # recieve data and address not more than 1024b
				print(data.decode("utf-8"))#printin data


				time.sleep(0.2)#delay jus for more stayble work
		except:#if any error just pass it
			pass
host = socket.gethostbyname(socket.gethostname())#taking host name and converting into address
port = 0

server_host = socket.gethostname()

server = (server_host,9090)#outr server is in our local mashine so we using the same addres but servers port differ from users

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# tcp,ip protocol
s.bind((host,port))#binding to host and port
s.setblocking(0)#set not blocing mode

alias = input("Name: ")#writing our users name

rT = threading.Thread(target = receving, args = ("RecvThread",s))#making thread for listening our server 
rT.start()

while shutdown == False:
	if join == False:
		s.sendto(("["+alias + "] => join chat ").encode("utf-8"),server)#when we create a new user we sendind message to server that we a connected
		join = True
	else:
		try:
			message = input()#trying to enter our message


			if message != "":#if message is not empty sending it to server
				s.sendto(("["+alias + "] :: "+message).encode("utf-8"),server)
			
			time.sleep(0.2)#making delay for more stayble work
		except:#if any error we sending massage that we are left from server and closing connection
			s.sendto(("["+alias + "] <= left chat ").encode("utf-8"),server)
			shutdown = True

rT.join()
s.close()