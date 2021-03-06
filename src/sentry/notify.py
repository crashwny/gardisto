import os

def notify(host, cause):
    f = open('/tmp/pingmsg.txt', 'w')
    log = open('/var/gardisto/notify.log', 'w')
    if checkForSnooze(host) == 1:
        return 0
    else:
        f.write("Good Morning, \n")
        f.write(host)
        f.write(" is alerting for" )
        f.write(cause)
        f.write(". Please see Gardisto logs./n-Gardisto")
        f.close()
        log.write(host)
        log.write("-")
        log.write(cause)
        log.write("\n")
        os.system("mutt -s 'Ping Check' pmcovert@buffaloist.com < /tmp/pingmsg.txt")

def checkForSnooze(hostName):
    con = sqlite3.connect('/var/gardisto/sentry.db')
    cursorObj = con.cursor()
    snooze = cursorObj.execute('SELECT snooze FROM hosts WHERE hostname IS "' + hostName + '";')
    return snooze
