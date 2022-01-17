import sqlite3

con = sqlite3.connect('/var/gardisto/sentry.db')
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
        for data in olddata:
            someData = data
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
        print("Gardisto Added:    ", somedata[9])
        print("Gardisto Key Added:", somedata[10])
        print("")

def printmany():
    hostlist = cursorObj.execute("SELECT hostname FROM hosts").fetchall()
    print(hostlist)
    #hostlist = cursorObj.fetchall()
    for host in hostlist:
        hostname = str(host[0])
        print(" ")
        prettyPrint(hostname)
        print(" ")

if __name__ == "__main__":
    printdata()
