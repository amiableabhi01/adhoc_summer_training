#!/usr/bin/python
import socket
#   type of ip V4  ,   type of protocol UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg=raw_input("enter any linux command: ")

s.sendto(msg,("192.168.43.135",8000))    

