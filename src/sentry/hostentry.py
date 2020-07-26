import subprocess
import os
import sqlite3
import time
from sentry import missingtable
con = sqlite3.connect('sentry.db')
cursorObj = con.cursor()

# sqlite> .schema hosts
# CREATE TABLE hosts(
# hostname TEXT NOT NULL,
# IP TEXT NOT NULL,
# lastup TEXT,
# lastdown TEXT,
# fqdn TEXT,
# site TEXT NOT NULL,
# type TEXT NOT NULL,
# parent TEXT NOT NULL
# );

def enterdata():
    hostname = input("Enter Hostname: ")
    IP = input("Enter host's IP address: ")
    fqdn = input("Enter host's FQDN, or leave blank if none: ")
    site = input("Enter host's site name: ")
    hostType = input("Enter host type, vm or bm: ")
    parent = input("If the host is a vm, please enter parent host's name: ")
    entrydata = (hostname, IP, fqdn, site, hostType, parent)
    # sship = "sentry@" + IP
    # subprocess.Popen(["/usr/bin/ssh-copy-id", sship], stdout=subprocess.PIPE)
    return entrydata
    # print(entrydata)
    print("Remember to add ssh keys for sentry to access your hosts!")

def processdata():
    try:
        cursorObj.execute('''INSERT INTO hosts(hostname, IP, fqdn, site, type, parent) VALUES(?, ?, ?, ?, ?, ?)''', enterdata())
        con.commit()
    except sqlite3.OperationalError:
        missingtable()
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


