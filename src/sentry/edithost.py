# edit a host's db entry
import sqlite3
from sentry import missingtable
con = sqlite3.connect('sentry.db')
cursorObj = con.cursor()

def oneHost(host):
    olddata = cursorObj.execute(
        "SELECT * FROM hosts WHERE hostname = ?", (host,)
    ).fetchall()    
    # olddata has to be interated through into a new variable so that the data can be interable
    for data in olddata:
        somedata = data

