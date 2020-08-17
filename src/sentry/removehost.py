import sqlite3
con = sqlite3.connect('sentry.db')
cursorObj = con.cursor()

# usage: remove a host from sentry by calling removehost.removehost(hostname)

def removehost(host):
    cursorObj.execute(
        "DELETE FROM hosts WHERE hostname = ?", (host,)
    )
    con.commit()
    print(host + " deleted!")

if __name__ == "__main__":
    removehost(host)

