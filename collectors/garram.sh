#!/usr/bin/env bash
# Sentry collector script for RAM stats

date +%Y%m%d%H%M >> /var/sentry/data/senmemory.data
free -m | tail -2 >> /var/sentry/data/senmemory.data

