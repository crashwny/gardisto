#!/usr/bin/env bash
# Gardisto collector script for CPU stats

date +%Y%m%d%H%M >> /var/gardisto/garcpu.data
sar | tail -2 | head -1 >> /var/gardisto/garcpu.data
