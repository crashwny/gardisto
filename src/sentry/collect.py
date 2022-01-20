import os, threading, configparser
from sentry import notify

def getAllColl():
    configFile = "/var/gardisto/gardisto.conf"
    config = configparser.ConfigParser()
    fpath = '/var/gardisto/collectors/'
    flist = os.listdir(path=fpath)
    fList = []
    for i in flist:
        fList.append(i.split("."))
    config.read(configFile)
    for i in fList:
        filepath = str("/var/gardisto/collectors/" + i[0] + "." + i[1] + "." + i[2])
        hostname = i[0]
        test = i[1].replace("gar", "")
        if test in config["SERVER"]:
            try:
                limit = float(config['SERVER'][test])
            except:
                limit = float(0)
        else:
            limit = float(1)
        fileObj = open(filepath, "r")
        data = fileObj.read()
        fileObj.close()
        if data is None:
            value = float(0)
        elif test == "ram":
            data = data.split(" ")
            while("" in data):
                data.remove("")
            totalswap = float(data[1])
            usedswap = float(data[2])
            print(usedswap)
            value = usedswap // totalswap
        elif test == "cpu":
            data = data.split(" ")
            while("" in data):
                data.remove("")
            print(data)
            rawvalue = data[-1]
            value = 1 // float(rawvalue.replace('\n', ''))
        else:
            try:
                value = float(data)
            except:
                value = float(0)
        if value < limit:
            None
        else:
            notify.notify(hostname, test)
        os.remove(filepath)

if __name__ == "__main__":
    getAllColl()
