#!/usr/bin/env bash
# Gardisto collector script for RAM stats

date +%Y%m%d%H%M >> /var/gardisto/garram.data
free -m | tail -2 >> /var/gardisto/garram.data
