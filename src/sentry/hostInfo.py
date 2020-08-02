# hostinfo: show host information
import sqlite3
con = sqlite3.connect('sentry.db')
cursorObj = con.cursor()

def showone(host):
    cursorObj.execute('''SELECT * FROM hosts WHERE hostname = ?''', (host,))
    data = cursorObj.fetchall()
    print(data)

def showall():
    cursorObj.execute("SELECT * FROM hosts")
    print(cursorObj.fetchall())

if __name__ == "__main__":
    showall()
