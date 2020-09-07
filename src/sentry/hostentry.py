import subprocess
import os
import sqlite3
import time
from sentry import missingtable, printdata
con = sqlite3.connect('/var/sentry/data/sentry.db')
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
    print("\n Remember to add ssh keys for sentry to access your hosts!\n ")
    return entrydata

def processdata():
    entrydata = enterdata()
    try:
        cursorObj.execute('''INSERT INTO hosts(hostname, IP, fqdn, site, type, parent) VALUES(?, ?, ?, ?, ?, ?)''', entrydata)
        con.commit()
    except sqlite3.OperationalError:
        missingtable.create()
        cursorObj.execute('''INSERT INTO hosts(hostname, IP, fqdn, site, type, parent) VALUES(?, ?, ?, ?, ?, ?)'''    , entrydata)
        con.commit()
    print("Data Inserted")
    printdata.printdata()
    print(" \n  ")
    more = input("Would you like to add another host? (y or n) \n")
    if more == "y":
        processdata()
    else:
        None

#def printdata():
#    cursorObj.execute('SELECT * FROM hosts')
#    rows = cursorObj.fetchall()
#    for row in rows:
#        print(row)

if __name__ == "__main__":
    os.system('clear')
    processdata()


