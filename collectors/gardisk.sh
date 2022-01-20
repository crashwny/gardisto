#!/usr/bin/env bash
# Gardisto system check - disk space

date +%Y%m%d%H%M >> /var/gardisto/gardisk.data
df -h | grep -iv snap | grep "100%\|[9][0-9]%" >> /var/gardisto/gardisk.data
df -h | grep -iv snap | grep "100%\|[9][0-9]%" |wc -l >> /var/gardisto/gardisk.data
