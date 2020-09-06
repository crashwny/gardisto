# edit a host's db entry
import sqlite3
from sentry import missingtable
con = sqlite3.connect('/var/sentry/data/sentry.db')
cursorObj = con.cursor()
from sentry import hostentry

def oneHost(host):
    olddata = cursorObj.execute(
        "SELECT * FROM hosts WHERE hostname = ?", (host,)
    ).fetchall()    
    # olddata has to be interated through into a new variable so that the data can be interable
    print(olddata)
    for data in olddata:
        somedata = data
#    newdata = hostentry.enterdata()
#    cursorObj.execute(
    print(somedata)
    hostName = somedata[0]
    ipAddr = somedata[1]
    fqdn = somedata[5]
    site = somedata[6]
    parent = somedata[8]
    sentryAdded = somedata[9]
    sentryKeyAdded = somedata[10]
    userAdded = somedata[11]
    userKeyAdded = somedata[12]

    print(hostName)
