import os, configparser, sqlite3
from datetime import datetime

def notify(host, cause):
    f = open('/tmp/pingmsg.txt', 'w')
    log = open('/var/gardisto/notify.log', 'a')
    if checkForSnooze(host) == 1:
        return 0
    else:
        message = "Good Morning, \n\n" + host + " is alerting for " + cause + ". Please see Gardisto logs. \n\n -Gardisto"
        f.write(message)
        f.close()
        now = str(datetime.now())
        logMessage = now + "\n" + host + " - " + cause + "\n"
        log.write(logMessage)
        log.close()
        os.system("mutt -s 'Ping Check' " + getEmailAddress() + " < /tmp/pingmsg.txt")

def checkForSnooze(hostName):
    con = sqlite3.connect('/var/gardisto/sentry.db')
    cursorObj = con.cursor()
    snooze = cursorObj.execute('SELECT snooze FROM hosts WHERE hostname IS "' + hostName + '";').fetchall()
    return snooze[0][0]

def getEmailAddress():
    config = configparser.ConfigParser()
    config.read('/var/gardisto/gardisto.conf')
    emailAddress = config['SERVER']['NOTIFY_EMAIL']
    return emailAddress
