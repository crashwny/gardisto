## Known Gardisto Bugs

### Server

#### Faulty Checks

The RAM and DISK checks erroneously report failures when they are OK

#### Notification emails

there is no space between "for" and the check name.

#### Snooze Add/edit

edithost
```
debtest01

    Which field would you like to change?

    1: hostname
    2: IP Address
    3: FQDN
    4: Site/Colocation
    5: Parent Host
    6: Gardisto User Added y/n?
    7: Gardisto Key Added y/n?
    8: Snooze Host


Enter the number:
8
Snooze on or off?
0
Traceback (most recent call last):
  File "/home/gardisto/.local/bin/gardisto", line 11, in <module>
    load_entry_point('Gardisto', 'console_scripts', 'gardisto')()
  File "/usr/src/gardisto/src/sentry/cli.py", line 36, in main
    edithost.oneHost(args.host)
  File "/usr/src/gardisto/src/sentry/edithost.py", line 91, in oneHost
    oneHost(host)
  File "/usr/src/gardisto/src/sentry/edithost.py", line 93, in oneHost
    processData(host, field, newdata)
  File "/usr/src/gardisto/src/sentry/edithost.py", line 96, in processData
    command = 'UPDATE hosts SET ' + field + ' = "' + newdata + '" WHERE hostname = "' + host + '"'
TypeError: must be str, not int
[gardisto@gardisto gardisto]$
```

#### statistics

all satellite stats stored on ind. hosts, and if a host goes down there is no access to these stats to help diagnose. This should be stored on the server and available.

### Satellite
