from socket import *
import thread
import sys
s=socket(AF_INET,SOCK_DGRAM)
host="127.10.0.0"
port=5000
nick=raw_input('Enter your name : ')
data=raw_input('Send a message to the server to connect : ')

s.sendto(nick+":"+data,(host,port))

def receive_function(key,thread_number=2):

    if(thread_number<2):
        return 0 
    while 1:
      
        data,addr=s.recvfrom(65536)
        print data
            
        if(key in data):
            send_function(data,1)
            break
    return 0
def send_function(key,thread_number=2):
    if(thread_number<2):
        return 0 
    while 1:
        data=raw_input()
        s.sendto(nick+":"+data,(host,port))
        if(key in data):
             receive_function(data,1)
             break
    return 0 
try:
    thread.start_new_thread(send_function,("bye",2,))

except:
    print 'Error in creating threads'
try:    
    thread.start_new_thread(receive_function,("bye",2,))

except:
    print 'Error in creating threads'
while 1: pass   
s.close()
del s
                                                                                                                                                   
