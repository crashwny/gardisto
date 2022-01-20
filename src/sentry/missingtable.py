import sqlite3
import subprocess
def create():
    con = sqlite3.connect('/var/gardisto/sentry.db')
    cursorObj = con.cursor()

    try:
        cursorObj.execute('''CREATE TABLE hosts(
        hostname TEXT NOT NULL,
        IP TEXT NOT NULL,
        status BOOLEAN NOT NULL default '0',
        lastup TEXT,
        lastdown TEXT,
        fqdn TEXT,
        site TEXT NOT NULL,
        type TEXT NOT NULL,
        parent TEXT NOT NULL,
        snooze BOOLEAN NOT NULL default '0',
        details TEXT
        );''')
        cursorObj.execute('''CREATE VIEW status_view AS SELECT hostname AS "Hostname", status AS "is down?", lastup AS "Last up", lastdown AS "Last down" FROM hosts;''')
        con.commit()
        cursorObj.close()
    except sqlite3.OperationalError:
        print("Something went wrong.")
    finally:
        print("missing table script complete")

if __name__ == '__main__':
    create()
