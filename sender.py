#!/usr/bin/python3
##for socket connection
import  socket 
##for encoding decoding
import base64
##run any more then one function in one time
import _thread
##socket connection
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
rec_ip = '127.0.0.6'
my_port = 9999
s.bind((rec_ip,my_port))
#function for sending msg
def msg_send():
	while True:        	 
		msg = (input("take an msg:")).encode()
		encrypted_msg=base64.b64encode(msg)
		s.sendto(encrypted_msg,("127.0.0.6",8888))
	 
#function for reciving msg		
def msg_rec():	
	while True:
		msg2=s.recvfrom(1000)
		decrypted_msg2 = base64.b64decode(msg2[0])
		print((decrypted_msg2.decode()))
_thread.start_new_thread(msg_send,())
_thread.start_new_thread(msg_rec,())
while True:
	pass

