import os
import sqlite3
import datetime
import threading
# import sys (for sys.exit(1)
from sentry import hostping, missingtable, notify, collect

#connect this to your database with next 2 lines
con = sqlite3.connect('/var/gardisto/sentry.db')
cursorObj = con.cursor()

def getlist():
    # get host list from database and convert to object python can read
    cursorObj.execute('SELECT hostname, ip FROM hosts')
    try:
        hostlist = cursorObj.fetchall()
    except sqlite3.OperationalError:
        hostlist = 0
        missingtable()
    return hostlist

def pinglist():
    # ping all hosts from getlist module
    hostlist = getlist()
    resultlist = []
    for a,b in hostlist:
        result = hostping.hostPing(b)
        if result == True:
            pingresult = 0
        else:
            pingresult = 1
        resultlist.append((a, pingresult))

    return resultlist

def hoststatus(host):
    # gets the last status for hosts from the database
    cursorObj.execute('SELECT status FROM hosts WHERE hostname = \'' + host + '\'')
    try:
        status = cursorObj.fetchall()
    except sqlite3.OperationalError as err:
        status = 0
        missingtable()
    return status

def updatestatus(host, status, date):
    # updates the new status on the database
    oldstat = hoststatus(host)
    oldstatus = oldstat[0]
    oldstatus = int(oldstatus[0])
    if oldstatus == 1:
        if status == 1:
            command = 'UPDATE hosts SET lastdown = "' + date + '"WHERE hostname = "' + host + '"'
        else:
            command = 'UPDATE hosts SET status = "0", lastup = "' + date + '" WHERE hostname = "' + host + '"'
    else:
        if status == 1:
            command = 'UPDATE hosts SET status = "1", lastdown = "' + date + '" WHERE hostname = "' + host + '"'
            notify.notify(host, "down to ping")
        else:
            command = 'UPDATE hosts SET status = "0", lastup = "' + date + '" WHERE hostname = "' + host + '"'
    cursorObj.execute(command)
    con.commit()
    return

def resultwrite():
    # iterates the writing of the results by calling updatestatus()
    resultlist = pinglist()
    print(resultlist)
    timenow = str(datetime.datetime.utcnow())
    for a, b in resultlist:
        updatestatus(a, b, timenow)

def start():
    #collthread.start()
    collect.getAllColl()
    resultwrite()
    con.close()

if __name__ == "__main__":
    start()
