#!/usr/bin/env bash
# Sentry collector script for CPU stats

date +%Y%m%d%H%M >> /var/sentry/data/sencpu.data
sar | tail -2 | head -1 >> /var/sentry/data/sencpu.data

