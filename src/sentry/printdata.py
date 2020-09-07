import sqlite3

con = sqlite3.connect('/var/sentry/data/sentry.db')
cursorObj = con.cursor()

def printdata():
    cursorObj.execute('SELECT * FROM hosts')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

def getdata(host):
    try:
        olddata = cursorObj.execute(
        "SELECT * FROM hosts WHERE hostname = ?", (host,)
        ).fetchall()
        # olddata has to be interated through into a new variable so that the data can be interable
        #print(olddata)
        for data in olddata:
            someData = data
        #    print(somedata)
        #    hostName = somedata[0]
        #    ipAddr = somedata[1]
        #    fqdn = somedata[5]
        #    site = somedata[6]
        #    parent = somedata[8]
        #    sentryAdded = somedata[9]
        #    sentryKeyAdded = somedata[10]
        #    userAdded = somedata[11]
        #    userKeyAdded = somedata[12]
        return someData
    except:
        #print("no Data Found")
        someData = "no"
        return someData
def prettyPrint(host):
    try:
        somedata = getdata(host)
    except:
        print("No Data Found")
        somedata = "no"
    print(somedata)
    if somedata == "no":
        print("No Data Found")
    else:
        print("Hostname:        ", somedata[0])
        print("IP Address:      ", somedata[1])
        print("FQDN:            ", somedata[5])
        print("Site:            ", somedata[6])
        print("Parent:          ", somedata[8])
        print("Sentry Added:    ", somedata[9])
        print("Sentry Key Added:", somedata[10])
        print("")

def printmany():
    hostlist = cursorObj.execute("SELECT hostname FROM hosts").fetchall()
    print(hostlist)
    #hostlist = cursorObj.fetchall()
    for host in hostlist:
        hostname = str(host)
        print(" ")
        prettyPrint(hostname)
        print(" ")

if __name__ == "__main__":
    printdata()
