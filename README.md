Gardisto
======

Utility for monitoring hosts/servers.

## Usage

To have Gardisto watch over your hosts after set up, add `gardisto run` to your crontab at your desired interval.
    For example, `1,11,21,31,41,51 * * * * gardisto run`

### gardisto Maintenance Commands
 - `gardisto addhost` To add hosts for Gardisto to monitor
 - `gardisto removehost [-host hostname]`
 - `gardisto edithost [-host hostname]`

### gardisto Monitoring Commands
 - `gardisto run` Runs the gardisto. Should be added to your crontab for a specified interval
 - `gardisto showstats [-stat name, -stats] [-host hostname]` Shows statistics for specified host or all hosts, all stats or one specified (coming soon)gardisto
 - `gardisto show [-host hostname, -all]` Shows information for specified host or for all hosts (single host works, multihost support coming soon)

## Installation from source

On the Gardisto server, install the package after you have cloned the repository, you'll want to run the following command from within the project directory:

```
pip3 install --user -e .
```

For notifications to work, the Gardisto server must have mutt configured and functioning. This package will not install or configure mutt.

### Server Configuration

The Gardisto server and each satellite host needs to have user 'gardisto', and satellites with their SSH key added and verified SSH access to Gardisto server. The central server should not have ssh keys on the satellites.
 - Run this command as root on the server: `~/gardisto/server-setup.sh`
 - Next, run this also as root: `scp -r satellite-setup.sh ./collectors username@satellitehostFQDN:/tmp/`


<!---
 - `useradd -m -s /bin/bash gardisto`
 - `passwd gardisto` and enter password
 - add this line to /etc/sshd_config:
    `Match User !root
        PasswordAuthentication no`
 - `mkdir -p /var/gardisto/collectors`
 - `chown -R gardisto:gardisto /var/gardisto`
 - and on the satellites, as user gardisto, `cd ~/.ssh; ssh-keygen -t rsa -b 4096 -f gardisto.rsa -N ""`
   - then `ssh-add gardisto.rsa; ssh-copy-id gardisto@[gardisto.server.ip]`
The configuration is in the base gardisto directory from gitlab, and must be put in /var/gardisto of the server and all satellites.
---->

## Adding Collectors to satellite hosts

On the server, in /home/gardisto/gardisto, run as root: `scp -r satellite-setup.sh ./collectors username@satellitehostFQDN:/tmp/`
Then on the satellite, as root, run: `/tmp/satellite-setup.sh` which afterwards will direct you to switch to user gardisto and run `~/bash setup2.sh`

<!---- sar:
sudo apt-get install sysstat
(or)
yum install sysstat
(or)
rpm -ivh sysstat-10.0.0-1.i586.rpm ----->



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
gardistoAdded BOOLEAN NOT NULL default '0',
gardistoKeyAdded BOOLEAN NOT NULL default '0',
userAdded BOOLEAN NOT NULL default '0',
userKeyAdded BOOLEAN NOT NULL default '0';
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `http://173.64.3.56:65524/gitlab/patrick/gardisto`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`
