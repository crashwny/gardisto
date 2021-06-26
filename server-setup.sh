#!/usr/bin/env bash 
# Gardisto Server Setup Script 

# Must be run as root! 
if [[ $(whoami) = 'root' ]]; then
    echo "You are root. Installing" 
else 
    echo "You are not root. This script must be run as root." 
    exit 1 
fi 

export PATH="$HOME/.local/bin:$PATH" 

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

if [[ $os_type = "apt" ]]; then 
    apt install -y git zip wget curl vim nano
    apt install python3-pip -y 
else 
    yum install -y git zip wget curl vim nano
    yum install python3-pip -y
fi 

cd /tmp 
wget http://173.64.1.227:65524/gitlab/patrick/gardisto/-/archive/main/gardisto-main.zip 
unzip gardisto-main.zip 
mv gardisto-main /home/gardisto/gardisto 
cd /home/gardisto/gardisto/ 
chown -R gardisto:gardisto /home/gardisto/gardisto/ 

read -p "Enter Gardisto's FQDN or IP address: " gardfqdn 
read -p "Enter an email address for notifications: " gardEmail 
sed "s/replace1/$gardfqdn/" /home/gardisto/gardisto/gardisto.conf > /var/gardisto/gardisto.conf 
sed -i "s/replace2/$gardEmail/" /var/gardisto/gardisto.conf 
sed -i "s/gardisto.server.ip/$gardfqdn/g" satellite-setup.sh 

echo "PATH=$HOME/.local/bin:$PATH" >> /etc/profile 

runuser -l gardisto -c 'pip3 install --user -e /home/gardisto/gardisto/'


