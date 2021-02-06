#!/usr/bin/env bash
# Gardisto Server Setup Script

# Must be run as root!
if [ $(whoami) = 'root' ]; then
	echo "You are root. Installing"
else
  echo "You are not root. This script must be run as root."
  exit 1
fi

if [ $(uname -a|grep el|wc -l) = 0 ]; then
	echo "using apt"
	os_type="apt"
else
	os_type="yum"
	echo "using yum"
fi

useradd -m -s /bin/bash gardisto
passwd gardisto
mkdir -p /var/gardisto/collectors
chown -R gardisto:gardisto /var/gardisto

read -p "Enter Gardisto's FQDN or IP address: " gardfqdn

sed "s/SERVER_FQDN=/SERVER_FQDN=$gardfqdn/" gardisto.conf > /var/gardisto/gardisto.conf

sed "s/gardisto.server.ip/$gardfqdn/" satellite-setup.sh
