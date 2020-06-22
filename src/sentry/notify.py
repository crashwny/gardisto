import os
def notify(host):
    f = open('/tmp/pingmsg.txt', 'w')
    f.write("Good Morning, \n")
    f.write(host)
    f.write(" is down. Please see Sentry logs./n-Sentry")
    f.close()
	
    os.system("mutt -s 'Ping Check' pmcovert@buffaloist.com < /tmp/pingmsg.txt")
    
    
    


