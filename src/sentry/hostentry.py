import subprocess
import os
import sqlite3
import time
from sentry import missingtable
con = sqlite3.connect('/var/sentry/data/sentry.db')
cursorObj = con.cursor()

def enterdata():
    hostname = input("Enter Hostname: ")
    IP = input("Enter host's IP address: ")
    fqdn = input("Enter host's FQDN, or leave blank if none: ")
    site = input("Enter host's site name: ")
    hostType = input("Enter host type, vm or bm: ")
    parent = input("If the host is a vm, please enter parent host's name: ")
    entrydata = (hostname, IP, fqdn, site, hostType, parent)
    print("Remember to add ssh keys for sentry to access your hosts!")
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
    printdata()

def printdata():
    cursorObj.execute('SELECT * FROM hosts')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    os.system('clear')
    processdata()


