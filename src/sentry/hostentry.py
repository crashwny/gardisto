import subprocess
import os
import sqlite3
import time
import re
import json
from sentry import missingtable, printdata
con = sqlite3.connect('/var/gardisto/sentry.db')
cursorObj = con.cursor()

def enterdata():
    hostname = input("Enter Hostname: ")
    IP = input("Enter host's IP address: ")
    fqdn = input("Enter host's FQDN, or leave blank if none: ")
    site = input("Enter host's site name: ")
    hostType = input("Enter host type, vm or bm: ")
    if hostType == "vm":
        parent = input("Please enter parent host's name: ")
    else:
        parent = "0"
    entrydata = (hostname, IP, fqdn, site, hostType, parent)
    print("\n Remember to add ssh keys for Gardisto to access your hosts!\n ")
    return entrydata

def processdata(hostData):
    try:
        cursorObj.execute('''INSERT INTO hosts(hostname, IP, fqdn, site, type, parent) VALUES(?, ?, ?, ?, ?, ?)''', hostData)
        con.commit()
    except sqlite3.OperationalError:
        missingtable.create()
        cursorObj.execute('''INSERT INTO hosts(hostname, IP, fqdn, site, type, parent) VALUES(?, ?, ?, ?, ?, ?)'''    , hostData)
        con.commit()
    print("Data Inserted")
    printdata.printdata()
    print(" \n  ")

def start():
    os.system('clear')
    processdata(enterdata())
    more = input("Would you like to add another host? (y or n) \n")
    if more == "y":
        processdata()
    else:
        None

def script():
    newHosts = os.listdir('/tmp')
    for i in newHosts:
        if re.match('garadd*', i):
            newData = open("/tmp/" + i, "r")
            newdata = json.loads(newData.read())
            data = jsonparse(newdata)
            processdata(data)
            newData.close()

def jsonparse(jdata):
    entrydata = (jdata[hostname], jdata[IP], jdata[fqdn], site, hostType, parent)

if __name__ == "__main__":
    start()
