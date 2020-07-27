# hostinfo: show host information
import sqlite3
con = sqlite3.connect('sentry.db')
cursorObj = con.cursor()

def showone(host):
    print("coming soon")

def showall():
    print("coming soon")
    cursorObj.execute("SELECT * FROM hosts")
    print(cursorObj.fetchall())

if __name__ == "__main__":
    showall()
