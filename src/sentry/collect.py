import os
import threading
import configparser
from sentry import notify

configFile = "/var/gardisto/gardisto.conf"
config = configparser.ConfigParser()

def getAllColl():
    fpath = '/var/gardisto/collectors/'
    flist = os.listdir(path=fpath)
    fList = []
    for i in flist:
        fList.append(i.split("."))
    config.read(configFile)
    for i in fList:
        filepath = str("/var/gardisto/collectors/" + i[0] + "." + i[1] + "." + i[2])
        hostname = i[0]
        test = i[1].strip("gar")
        if test in config["SERVER"]:
            limit = float(config['SERVER'][test])
        else:
            limit = 1
        fileObj = open(filepath, "r")
        data = fileObj.read()
        if test = "ram":
            data = data.split(" ")
            while("" in data):
                data.remove("")
            totalswap = float(data[1])
            usedswap = float(data[2])
            value = usedswap / totalswap
        elif test = "cpu":
            data = data.split(" ")
            while("" in data):
                data.remove("")
            value = float(data[-1])
        else:
            value = data
        if value > limit:
            return 0
        else: notify.notify()
        os.remove(filepath)

if __name__ == "__main__":
    getAllColl()
