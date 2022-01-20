#!/usr/bin/env bash
# script to copy necessary files to satellites

read -p "input destination IP or FQDN: " target_fqdn
read -p "input username on that host: " target_user
target_address="$target_user@$target_fqdn"
scp satellite-setup.sh collectors/* "$target_user"@"$target_fqdn":/tmp/
