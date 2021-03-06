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
	# echo "using apt"
	os_type="apt"
else
	os_type="yum"
	# echo "using yum"
fi

useradd -m -s /bin/bash gardisto
passwd gardisto
mkdir -p /var/gardisto/collectors
touch /var/gardisto/notify.log
chown -R gardisto:gardisto /var/gardisto

if [ $os_type = "apt" ]; then
	apt install git -y
	apt install zip -y
else
	yum install git -y
	yum install zip -y
fi

cd /tmp
wget https://github.com/crashwny/gardisto/archive/main.zip
unzip main.zip
mv gardisto-main/ /home/gardisto/
cd /home/gardisto/gardisto-main/
chown -R gardisto:gardisto /home/gardisto/gardisto-main/

read -p "Enter Gardisto's FQDN or IP address: " gardfqdn

sed "s/SERVER_FQDN=/SERVER_FQDN=$gardfqdn/" gardisto.conf > /var/gardisto/gardisto.conf

sed -i "s/gardisto.server.ip/$gardfqdn/" satellite-setup.sh

runuser -l gardisto -c 'pip3 install --user -e /home/gardisto/gardisto-main/'
