#!/usr/bin/env bash
# Gardisto collector script for temperature stats

date +%Y%m%d%H%M >> /var/gardisto/gartemp.data
output=$(sensors)
outPut=$(sensors|grep temp |grep "[6-9][0-9]"|tr -d "\n")
set -- $outPut
echo $output >> /var/gardisto/gartemp.data
echo $outPut >> /var/gardisto/gartemp.data
