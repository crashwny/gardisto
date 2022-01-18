Gardisto
======

Utility for monitoring hosts/servers.

## Usage

To have Gardisto watch over your hosts after set up, add `gardisto run` to your crontab at your desired interval.
    For example, `*/10 * * * * /home/gardisto/.local/bin/gardisto run`

On the Satellite hosts, add `collector.sh` to your crontab.
    For example, `*/10 * * * * /var/gardisto/collectors/collector.sh`

### gardisto Maintenance Commands
 - `gardisto addhost` To add hosts for Gardisto to monitor
 - `gardisto removehost [-host hostname]`
 - `gardisto edithost [-host hostname]`

### gardisto Monitoring Commands
 - `gardisto run` Runs the gardisto. Should be added to your crontab for a specified interval
 - `gardisto showstats [-stat name, -stats] [-host hostname]` Shows statistics for specified host or all hosts, all stats or one specified (coming soon)
 <!--- fix this ^ --->
 - `gardisto show [-host hostname, -all]` Shows information for specified host or for all hosts

## Installation from source
<!---
From a clean RHEL/Rocky install, download the sourcecode from https://gardisto.org/latest.tar.gz. You must create a user `gardisto` that does NOT have sudo access. As user `gardisto`, extract sourcecode to `/home/gardisto/gardisto/`, cd to that directory, and run `pip3 install --user -e /usr/src/gardisto/`.

Create the directory `/var/gardisto` and copy the gardisto.conf and the whole `collectors` file into it.
--->
From a clean RHEL/Rocky install, download the sourcecode from `https://gardisto.org/latest.tar.gz` Extract the file to /home/gardisto/gardisto/, and run `bash /home/gardisto//gardisto/server-setup.sh` as root. You will have to input a password for the gardisto user and enter the FQDN or IP address that the gardisto server can be reached by satellite servers.

For notifications to work, the Gardisto server must have mutt configured and functioning. This package will not install or configure mutt. Normally mutt can be installed with `yum install -y sendmail mutt tar` and then in the gardisto home folder, create a `.muttrc` configuration file. Use a search engine to find help to set it up for your email provider.  

### Server Configuration

The configuration file is found in /var/gardisto/gardisto.conf.

## Adding Collectors to satellite hosts

On the server, run as root:
`scp -r /home/gardisto/gardisto/satellite-setup.sh /home/gardisto/gardisto/collectors [username]@[satellitehostFQDN]:/tmp/`

Then on the satellite, as root, run:
`/tmp/satellite-setup.sh`
which afterwards will direct you to switch to user gardisto and run
`~/bash setup2.sh`

Once the installation scripts are done, navigate to /var/gardisto/collectors/ and finish configuring the desired checks. You can run the individual gar* scripts to make sure your host handles them properly. If you do not wish to run a particular script, you can rm that script. If you want Gardisto to monitor a particular service, you must edit garservice.sh appropriately. there are a small number of prewritten checks for common services, which you can uncomment to run. Or, write your own line following the same pattern as the rest.

## Database Requirements

This project uses SQlite3.

Table setup:

```
sqlite> .schema hosts
CREATE TABLE hosts(
hostname TEXT NOT NULL,
IP TEXT NOT NULL,
status BOOLEAN NOT NULL default '0',
lastup TEXT,
lastdown TEXT,
fqdn TEXT,
site TEXT NOT NULL,
type TEXT NOT NULL,
parent TEXT NOT NULL,
snooze BOOLEAN NOT NULL default '0';
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. ask for access to the repository.
3. `cd` into the repository
4. `git checkout dev`
5. Activate virtualenv: `pipenv shell`
6. Install dependencies: `pipenv install`
