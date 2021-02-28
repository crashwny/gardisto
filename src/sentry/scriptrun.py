import json
import os
from sentry import hostentry, edithost, removehost

# '{"toDo": "", "hostname": "", "ip": "", "fqdn": "", "site": "", "hostType": "", "parent": "", "gardistoAdded": "", "gardistoKeyAdded": "", "userAdded": "", "userKeyAdded": "", "snooze": ""}'

#hostname, IP, fqdn, site, type, parent

def jsonStart(scriptJson):
    data = json.loads(scriptJson)
    if data["toDo"] == "addhost":
        addHost(data)
    elif data["toDo"] == "removehost":
        removeHost(data["hostname"])
    elif data["toDo"] == "edithost":
        editHost(data)
    else:
        print("Script Failed!")
        return 1
    return 0

def addHost(data):
    dataList = (data["hostname"], data["ip"], data["fqdn"], data["site"], data["hostType"], data["parent"])
    hostentry.processdata(dataList)

def removeHost(hostName):
    removehost.removehost(hostName)

def editHost(data):
    editHost

def from_cli():
    f = open("/var/gardisto/garadd*", "r")
    jsonStart(f.read())
    f.close()

if __name__ == "__main__":
    from_cli():
    return 0
