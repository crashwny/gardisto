# hostinfo: show host information
import sqlite3
con = sqlite3.connect('/home/sentry/data/sentry.db')
cursorObj = con.cursor()

def showone(host):
    cursorObj.execute('''SELECT * FROM hosts WHERE hostname = ?''', (host,))
    data = cursorObj.fetchall()
    print(data)

def showall():
    cursorObj.execute("SELECT * FROM hosts")
    print(cursorObj.fetchall())

def printpretty(host):
    cursorObj.execute("SELECT * FROM hosts WHERE hostname = ?", (host,))
    colTitles = [tuple[0] for tuple in cursorObj.description]
    hostData = cursorObj.fetchall()
    for data in hostData:
        hostdata = data
    displayData = colTitles + hostdata
    for data in displayData:
        print(data)


if __name__ == "__main__":
    showall()
