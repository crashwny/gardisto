#!/usr/bin/env bash
# Sentry system check - disk 

date +%Y%m%d%H%M >> /var/sentry/data/sendisk.data
df -h | grep 100%\|[9][0-9]% >> /var/sentry/data/sendisk.data
df -h | grep 100%\|[9][0-9]% |wc -l >> /var/sentry/data/sendisk.data

