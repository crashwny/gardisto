Sentry
======

Utility for monitoring hosts/servers.

## Usage

To have sentry watch over your hosts after set up, add `sentry run` to your crontab at your desired interval. 
    For example, `1,11,21,31,41,51 * * * * sentry run`

Every host needs to have user 'sentry' with an SSH key added and verified SSH access. Run the following commands as root:
 - `useradd -m -s /bin/bash sentry`
 - `passwd sentry` and enter password
 - add this line to /etc/sshd_config: 
    `Match User !root
        PasswordAuthentication no`

### Sentry Maintenance Commands
 - `sentry addhost` To add hosts for Sentry to monitor
 - `sentry removehost -[hostname]` (coming soon)
 - `sentry edithost -[hostname]` (coming soon)

### Sentry Monitoring Commands
 - `sentry run` Runs the Sentry. Should be added to your crontab for a specified interval
 - `sentry showstats [--all] [--host hostname] [--stat] [--stats]` Shows statistics for specified host or all hosts, all stats or one specified (coming soon)
 - `sentry show -[hostname or all]` Shows information for specified host or for all hosts (coming soon)

## Installation from source

To install the package after you have cloned the respository, you'll want to run the following command from within the project directory:

```
pip3 install --user -e .
```

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
sentryAdded BOOLEAN NOT NULL default '0',
sentryKeyAdded BOOLEAN NOT NULL default '0',
userAdded BOOLEAN NOT NULL default '0',
userKeyAdded BOOLEAN NOT NULL default '0';
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `http://173.64.3.56:65524/gitlab/patrick/sentry-public`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`

