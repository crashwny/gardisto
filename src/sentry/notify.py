import os
def notify():
    f = open('/tmp/pingmsg.txt', 'w')
    f.write("""\
            Greetings,
            
            I have detected a server error!  Please check the Sentry Log on 192.168.1.24.
            
            - Sentry
            """)
    f.close()
	
    os.system("mutt -s 'Ping Check' pmcovert@buffaloist.com < /tmp/pingmsg.txt")
    
    
    


