#!/usr/bin/env bash
# Gardisto collector script for ProxMox Disk Health

date +%Y%m%d%H%M >> /var/gardisto/garpmxdisk.data
if [ $(zpool status -x|wc -l) > 1]; then
    echo $(zpool status) > /var/gardisto/garpmxdisk.data
else
    echo "0" > /var/gardisto/garpmxdisk.data
