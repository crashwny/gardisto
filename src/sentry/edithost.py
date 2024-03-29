# edit a host's db entry

import sqlite3
from sentry import missingtable
con = sqlite3.connect('/var/gardisto/sentry.db')
cursorObj = con.cursor()
from sentry import hostentry, printdata

def oneHost(host):
    somedata = printdata.getdata(host)
    hostName = somedata[0]
    ipAddr = somedata[1]
    fqdn = somedata[5]
    site = somedata[6]
    parent = somedata[8]
    snooze = somedata[13]

    print(hostName)
    print('''
    Which field would you like to change?

    1: hostname
    2: IP Address
    3: FQDN
    4: Site/Colocation
    5: Parent Host
    6: Snooze Host

    ''')
    choice = input("Enter the number:\n")

    if choice == "1":
        field = "hostname"
        print("Old hostname is " + hostName)
        newdata = input("What is the new hostname?\n")
    elif choice == "2":
        field = "IP"
        print("Old IP address is " + ipAddr)
        newdata = input("What is the new IP Address?\n")
    elif choice == "3":
        field = "fqdn"
        print("Old FQDN is " + fqdn)
        newdata = input("What is the new FQDN?\n")
    elif choice == "4":
        field = "site"
        print("Old Site name is " + site)
        newdata = input("What is the new site name?\n")
    elif choice == "5":
        field = "parent"
        print("Old Parent host name is " + parent)
        newdata = input("What is the new parent host name?\n")
    elif choice == "6":
        field = "snooze"
        newdata = input("Snooze on or off? \n")
        if newdata == "on":
            newdata = "1"
        else:
            newdata = "0"
    else:
        print("Please Make A Valid Selection")
        oneHost(host)

    processData(host, field, newdata)

def processData(host, field, newdata):
    command = 'UPDATE hosts SET ' + field + ' = "' + newdata + '" WHERE hostname = "' + host + '"'
    #print(command)
    cursorObj.execute(command)
    con.commit()
