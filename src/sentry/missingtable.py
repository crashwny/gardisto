import sqlite3

con = sqlite3.connect('sentry.db')
cursorObj = con.cursor()

cursorObj.execute('''CREATE TABLE hosts(
hostname TEXT NOT NULL,
IP TEXT NOT NULL,
lastup TEXT,
lastdown TEXT,
fqdn TEXT,
site TEXT NOT NULL,
type TEXT NOT NULL,
parent TEXT NOT NULL
);''')
con.commit()
cursorObj.close()

