# hostinfo: show host information
import sqlite3
con = sqlite3.connect('sentry.db')
cursorObj = con.cursor()

def showone(host):
    command="SELECT * FROM hosts WHERE hostname = '" + host + "'"
    cursorObj.execute(command)
    data = cursorObj.fetchall()
    print(data)
def showall():
    cursorObj.execute("SELECT * FROM hosts")
    print(cursorObj.fetchall())

if __name__ == "__main__":
    showall()
