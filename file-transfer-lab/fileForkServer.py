#! /usr/bin/env python3
import sys
sys.path.append("../lib")       # for params

import sys, os, socket, params


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

while True:
    sock, addr = lsock.accept()

    from framedSock import framedSend, framedReceive

    rc = os.fork()

    #if not os.fork():
    if rc == 0:
        print("new child process handling connection from", addr)
        while True:
            header = framedReceive(sock, debug) #recieve header 
            header = header.decode() #decode from bytes to str
            if debug: 
                print("rec'd: ", header)
            if not header:
                if debug: print("child exiting")
                sys.exit(0)


            #fl = open()

            else:
                payload = framedReceive(sock, debug) #actual data
                write = open('new'+header, 'wb') # write file
                write.write(payload)


            payload += b"!"             # make emphatic!
            framedSend(sock, payload, debug)

