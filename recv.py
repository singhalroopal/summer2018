#!/usr/bin/python3
import socket
import _thread
import base64

rec_ip = "127.0.0.6"
rec_port = 8888
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#binding ip and port to create socket
s.bind((rec_ip,rec_port))
#function for reciving msg
def recv_msg():
	while True:
		msg = s.recvfrom(1000)
		decrypted_msg = base64.b64decode(msg[0])
		print((decrypted_msg.decode()))

#function for sending msg		
def send_msg():
	while True:
		msg2 = (input("take an msg:")).encode()
		encrypted_msg=base64.b64encode(msg2)
		s.sendto(encrypted_msg,("127.0.0.6",9999))
_thread.start_new_thread(recv_msg,())
_thread.start_new_thread(send_msg,())
while True:
	pass
