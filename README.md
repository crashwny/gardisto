Sentry
======

Utility for watching hosts/servers for uptime.

## Usage

To have sentry watch over your hosts after set up, add `sentry run` to your crontab at your desired interval. 
    For example, `1,11,21,31,41,51 * * * * sentry run`

### Sentry Maintenance Commands
 - `sentry addhost` To add hosts for Sentry to monitor
 - `sentry removehost -[hostname]`
 - `sentry edithost -[hostname]`

### Sentry Monitoring Commands
 - `sentry run` Runs the Sentry. Should be added to your crontab for a specified interval
 - `sentry showstats -[hostname or all] -[stat or all]` Shows statistics for specified host or all hosts, all stats or one specified
 - `sentry show -[hostname or all]` Shows information for specified host or for all hosts

## Installation from source

To install the package after you have closed the respoistory, you'll want to run the following command from within the project directory:

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
status TEXT,
lastup TEXT,
lastdown TEXT,
fqdn TEXT,
site TEXT NOT NULL,
type TEXT NOT NULL,
parent TEXT NOT NULL
);
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `http://173.64.3.56:65524/gitlab/patrick/sentry-public`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`

