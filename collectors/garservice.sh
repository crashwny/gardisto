#!/usr/bin/env bash
# Sentry Service status script
# uncomment the services that are pertinent to the host monitoring

date +%Y%m%d%H%M > /var/sentry/data/senservice.data

#gitlab
#systemctl status gitlab-runsvdir |grep fail|wc -l > /var/sentry/data/senservice.data

#rocketchat
#systemctl status mongod rocketchat | grep fail| wc -l > /var/sentry/data/senservice.data

#zoneminder
#systemctl status mariadb zoneminder | grep fail| wc -l > /var/sentry/data/senservice.data

