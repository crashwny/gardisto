#!/usr/bin/env bash
# Gardisto Satellite Setup Script

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

echo '#!/usr/bin/env bash
# Gardisto Satellite Setup Script Part 2
mkdir ~/.ssh
cd ~/.ssh; ssh-keygen -t rsa -b 4096 -f gardisto.rsa -N ""
ssh-add gardisto.rsa; ssh-copy-id gardisto@[gardisto.server.ip]
chmod 700 ~/.ssh
'>/home/gardisto/setup2.sh

chown gardisto:gardisto /home/gardisto/setup2.sh

su gardisto -c "bash /home/gardisto/setup2.sh"
