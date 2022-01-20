#!/usr/bin/env bash
# Gardisto collector script for CPU stats

date +%Y%m%d%H%M >> /var/gardisto/garcpu.data
sar | tail -2 | head -1 | awk '{ print substr( $0, 1, length($0)-2 ) }' >> /var/gardisto/garcpu.data
