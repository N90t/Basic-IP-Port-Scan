#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)    #Setting timeout helps in getting response faster

#You can embed speicific ipaddress & port if you want check at specific intervals.
#host = "IPADDRESS"
#port = 80 

#Here, given an option to provide an input which is feasible.
host = input("Enter IP you want to scan")
port = int(input("Enter port you want to scan")

def portscan():
    if s.connect_ex((host,port)):
        print("The port is closed")
    else:
        print("The port is open")

portscan()
