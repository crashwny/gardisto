#!/usr/bin/env bash
# Gardisto Server Setup Script

# Must be run as root!
if [ $(whoami) = 'root' ]; then
	echo "You are root. Installing"
else
  echo "You are not root. This script must be run as root."
  exit 1
fi

useradd -m -s /bin/bash gardisto
passwd gardisto
mkdir -p /var/gardisto/collectors
chown -R gardisto:gardisto /var/gardisto

# sed -i '1s/^[^=]*=//' gardisto.conf
sed '1s/^[^=]*=//' gardisto.conf > /var/gardisto/gardisto.conf

sed -i "s/[gardisto.server.ip]/$(hostname)/g" satellite-setup.sh
