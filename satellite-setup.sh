#!/usr/bin/env bash
# Gardisto Satellite Setup Script

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
	apt install sysstat
	systemctl start sysstat
	systemctl enable sysstat
	sed -i s/'ENABLED="false"'/'ENABLED="true"'/ /etc/default/sysstat
else
	os_type="yum"
	# echo "using yum"
	yum install sysstat
fi

useradd -m -s /bin/bash gardisto
passwd gardisto
mkdir -p /var/gardisto/collectors
chown -R gardisto:gardisto /var/gardisto

echo '#!/usr/bin/env bash
# Gardisto Satellite Setup Script Part 2
mkdir ~/.ssh
cd ~/.ssh; ssh-keygen -t rsa -b 4096 -f gardisto.rsa -N ""
eval `ssh-agent -s`
ssh-add gardisto.rsa; ssh-copy-id gardisto@gardisto.server.ip
chmod 700 ~/.ssh
scp gardisto@gardisto.server.ip:/var/gardisto/gardisto.conf /var/gardisto/gardisto.conf
scp gardisto@gardisto.server.ip:/home/gardisto/gardisto-main/collectors/* /var/gardisto/collectors/
scp gardisto@gardisto.server.ip:/home/gardisto/gardisto-main/satellite-hostentry.sh /var/gardisto/
sleep 10
bash /var/gardisto/satellite-hostentry.sh
'>/home/gardisto/setup2.sh

chown gardisto:gardisto /home/gardisto/setup2.sh
cp -r /tmp/collectors /var/gardisto/
chown -R gardisto:gardisto /var/gardisto/collectors

# su gardisto -c "bash /home/gardisto/setup2.sh"
clear
echo "***********"
echo "switch to user gardisto and run:"
echo "bash /home/gardisto/setup2.sh"
echo "***********"
