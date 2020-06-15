Sentry
======

Utility for watching hosts/servers for uptime.

## Usage

Run sentry --hostentry to enter hosts to monitor, then add sentry --run to your crontap for the desired interval. 

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
lastup TEXT,
lastdown TEXT,
fqdn TEXT,
site TEXT NOT NULL,
type TEXT NOT NULL,
parent TEXT NOT NULL,
status TEXT
);
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `http://173.64.3.56:65524/gitlab/patrick/sentry-public`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`

