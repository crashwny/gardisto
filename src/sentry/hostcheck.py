import os
import sqlite3
import datetime
# import sys (for sys.exit(1)
from sentry import hostping, missingtable

#connect this to your database with next 2 lines
con = sqlite3.connect('sentry.db')
cursorObj = con.cursor()

# this block is to remind me of the database fields
# sqlite> .schema hosts
# CREATE TABLE hosts(
# hostname TEXT NOT NULL,
# IP TEXT NOT NULL,
# lastup TEXT,
# lastdown TEXT,
# fqdn TEXT,
# site TEXT NOT NULL,
# type TEXT NOT NULL,
# parent TEXT NOT NULL,
# status TEXT
# );

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
    #     cmd = 'ping -c 1 -Aq ' + b + ' > /dev/null 2>&1'
    #     result = os.system(cmd)
    #     if result == 0:
    #         pingresult = 1
    #     else:
    #         pingresult = 0
    #     resultlist.append((a, pingresult))
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
            return
        else:
            command = 'UPDATE hosts SET status = "0", lastdown = "' + date + '" WHERE hostname = "' + host + '"'
    else:
        if status == 1:
            command = 'UPDATE hosts SET status = "1", lastup = "' + date + '" WHERE hostname = "' + host + '"'
        else:
            return
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

if __name__ == "__main__":
    start()

def start():
    resultwrite()
    con.close()

