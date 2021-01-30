#!/usr/bin/env bash
# Gardisto Service status script
# uncomment the services that are pertinent to the host monitoring

date +%Y%m%d%H%M > /var/gardisto/garservice.data

#gitlab
#systemctl status gitlab-runsvdir |grep fail|wc -l > /var/gardisto/garservice.data

#rocketchat
#systemctl status mongod rocketchat | grep fail| wc -l > /var/gardisto/garservice.data

#zoneminder
#systemctl status mariadb zoneminder | grep fail| wc -l > /var/gardisto/garservice.data
