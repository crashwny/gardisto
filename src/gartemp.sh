#!/usr/bin/env bash
# Gardisto collector script for temperature stats

date +%Y%m%d%H%M >> /var/gardisto/gartemp.data
outPut=$(sensors|grep temp |grep "[6-9][0-9]"|tr -d "\n")
set -- $outPut
echo $outPut >> /var/gardisto/gartemp.data
