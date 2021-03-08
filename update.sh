#!/usr/bin/env bash
# updating satellites from Gardisto 0.2.2 to 0.2.3

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
    systemctl restart sysstat
    apt install lm-sensors
else
	os_type="yum"
	# echo "using yum"
	yum install sysstat
    systemctl start sysstat
	systemctl enable sysstat
    yum install lm_sensors
fi

serverfqdn=$(cat /var/gardisto/gardisto.conf|grep SERVER_FQDN|sed 's/^[^=]*=//')
serverfqdn=$(echo $serverfqdn|sed 's/ //g')

echo "#!/usr/bin/env bash
# Gardisto Satellite Update Script Part 2
scp gardisto@$serverfqdn:/var/gardisto/update-package.tar.gz /var/gardisto/
tar -xcf /var/gardisto/update-package.tar.gz
mv -f /var/gardisto/update-package/gardisto.conf /var/gardisto/gardisto.conf
mv -f /var/gardisto/update-package/collectors/* /var/gardisto/collectors/

">/home/gardisto/update2.sh

chown gardisto:gardisto /home/gardisto/update2.sh

clear
echo "***********"
echo "switch to user gardisto and run:"
echo "bash /home/gardisto/update2.sh"
echo "***********"
