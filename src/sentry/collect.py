import os
import threading
from gardisto import notify

cputhread = threading.Thread(target=cpucollect args=(cpufiles))
diskthread = threading.Thread(target=diskcollect args=(diskfiles))
ramthread = threading.Thread(target=ramcollect args=(ramfiles))
servicethread = threading.Thread(target=servicecollect args(servicefiles))

def collect():
    cpufiles = []
    diskfiles = []
    ramfiles = []
    servicefiles = []
    fpath = '/var/gardisto/collectors/'
    # newfiles = []
    flist = os.listdir(path=fpath)
    for i in flist:
        # newfiles.amend(i)
        if i.find("cpu") > -1:
            cpufiles.append(i)
        elif i.find("disk") > -1:
            diskfiles.append(i)
        elif i.find("ram") > -1:
            ramfiles.append(i)
        elif i.find("service"):
            servicefiles.append(i)
        else:
            return None
    #cpucollect(cpufiles)
    #diskcollect(diskfiles)
    #ramcollect(ramfiles)
    #servicecollect(servicefiles)
    cputhread()
    diskthread()
    ramthread()
    servicethread()

def cpucollect(cpufiles):
    # end thread if no cpu files
    if cpufiles == []:
        return None

    # get cpu test value
    conf = "/var/gardisto/gardisto.conf"
    confobj = open(conf, "r")
    confread = confobj.read()
    confread = confread.split("\n")
    for i in confread:
        if i.find("CPU") > -1:
            limit = i
    limit = limit.split("=")
    limit = limit[1]
    limit = float(limit)

    # get data from satellites
    for f in cpufiles:
        filepath = "/var/gardisto/collectors/" + f
        fileobj = open(filepath, "r")
        data = str(fileobj.read())
        data = data.split(" ")
        while("" in data):
            data.remove("")
        value = float(data[-1])
        # get hostname
        hostname = f.split(".")
        hostname = hostname[0]
        # test the value
        if value > limit:
            return None
        else:
            notify(hostname, "high CPU usage")
        fileobj.close()
        # then delete the fileobj
        os.remove(filepath)

def diskcollect(diskfiles):
    if diskfiles == []:
        return None

    # get disk test value
    conf = "/var/gardisto/gardisto.conf"
    confobj = open(conf, "r")
    confread = confobj.read()
    confread = confread.split("\n")
    for i in confread:
        if i.find("DISK") > -1:
            limit = i
    limit = limit.split("=")
    limit = limit[1]
    limit = float(limit)

    # get data from satellites
    for f in diskfiles:
        filepath = "/var/gardisto/collectors/" + f
        fileobj = open(filepath, "r")
        data = str(fileobj.read())
        data = data.split("\n")
        while("" in data):
            data.remove("")
        value = float(data[-1])
        # get hostname
        hostname = f.split(".")
        hostname = hostname[0]

        # test the value
        if value < limit:
            return None
        else:
            notify(hostname, "high disk usage")
        fileobj.close()
        # then delete the fileobj
        os.remove(filepath)

def ramcollect(ramfiles):
    if ramfiles == []:
        return None

    # get ram test value
    conf = "/var/gardisto/gardisto.conf"
    confobj = open(conf, "r")
    confread = confobj.read()
    confread = confread.split("\n")
    for i in confread:
        if i.find("RAM") > -1:
            limit = i
    limit = limit.split("=")
    limit = limit[1]
    limit = float(limit)

    # get data from satellites
    for f in ramfiles:
        filepath = "/var/gardisto/collectors/" + f
        fileobj = open(filepath, "r")
        data = str(fileobj.read())
        data = data.split("\n")
        while("" in data):
            data.remove("")
        value = float(data[-1])
        # get hostname
        hostname = f.split(".")
        hostname = hostname[0]

        # test the value
        if value < limit:
            return None
        else:
            notify(hostname, "high memory usage")
        fileobj.close()
        # then delete the fileobj
        os.remove(filepath)

def servicecollect(servicefiles):
    if servicefiles == []:
        return None
    do stuff

if __name__ == "__main__":
    collect()
