#!/bin/bash

NewIp="$(curl ifconfig.me)"
echo $NewIp
if [[ -e /home/patrick/oldip.log ]]
then
  OldIp="$(cat /home/patrick/oldip.log)"
else
  touch /home/patrick/oldip.log
fi
echo $OldIp
echo $NewIp
if [[ $OldIp != $NewIp ]]
then
  echo "Your IP has changed"
  echo $NewIp > /home/patrick/oldip.log
#  echo \n >> ~/bin/.oldip.txt
  mutt -s "IP Check" crashwny@gmail.com < /home/patrick/oldip.log
#  mail -s "IP Check" r.martinez@tarvos.io < /home/patrick/oldip.log
else
  echo "All is well"
fi

