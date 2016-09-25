from socket import *
import thread
s=socket(AF_INET,SOCK_DGRAM)
host="127.10.0.0"
port=5000
s.bind((host,port))
addr_list=[]
print 'Server started on port 5000'
def broadcast(addr,data):
    
    for adrs in addr_list:
        if(adrs!=addr):
            try: 
                s.sendto(data,adrs)
                
            
            except:
               addr_list.remove(adrs)
               print adrs," is not online"  
    return 0     
while 1:    
    data,addr=s.recvfrom(65536)
    
    if(addr not in addr_list):
        addr_list.append(addr)
    try:
        thread.start_new_thread(broadcast,(addr,data,))
        if("bye" in data):
            break  
    except:
        print 'Error in creating a thread' 
settimeout(2);      
s.close()
del s

