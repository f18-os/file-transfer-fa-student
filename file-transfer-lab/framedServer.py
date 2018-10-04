#! /usr/bin/env python3
import sys
sys.path.append("../lib")       # for params
import re, socket, params

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)

sock, addr = lsock.accept()

print("connection rec'd from", addr)


from framedSock import framedSend, framedReceive

while True:
    header = framedReceive(sock, debug)
    header = header.decode()
    if debug: 
        print("rec'd: ", header)
    if not header:
        if debug: print("child exiting")
        sys.exit(0)

    
    #fl = open()
    
    else:
        payload = framedReceive(sock, debug)
        write = open('new'+header, 'wb')
        write.write(payload)
        
