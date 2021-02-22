#!/usr/bin/env bash
# Gardisto Service status script
# uncomment the services that are pertinent to the host monitoring

date +%Y%m%d%H%M > /var/gardisto/garservice.data

#gitlab
#systemctl status gitlab-runsvdir |grep -i fail|wc -l > /var/gardisto/garservice.data

#rocketchat
#systemctl status mongod rocketchat | grep -i fail| wc -l > /var/gardisto/garservice.data

#zoneminder
#systemctl status mariadb zoneminder | grep -i fail| wc -l > /var/gardisto/garservice.data

#proxmox
#systemctl status pve* |grep -i fail| wc -l >/var/gardisto/garservice.data

#apache
#systemctl status httpd  |grep -i fail| wc -l >/var/gardisto/garservice.data

#apache2
#systemctl status apache2  |grep -i fail| wc -l >/var/gardisto/garservice.data
