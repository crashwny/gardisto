#!/usr/bin/env bash
# Gardisto Collector Script to run all collectors and send data to Gardisto server
collist=$(ls /var/gardisto/collectors/)
serverfqdn=$(cat /var/gardisto/gardisto.conf|grep SERVER_FQDN|sed 's/^[^=]*=//')
#this should be made into a vertical list
ls /var/gardisto/collectors/ |sed 's/ /\n/gp' > /tmp/collist.txt
#then, interate through this list to run the script, tail the log file
for i in $(cat /tmp/collist.txt)
do
  /var/gardisto/collectors/$i
done
#create a file to send using $hostname and $filename
ls /var/gardisto/ |grep data |sed 's/ /\n/gp' > /tmp/datalist.txt
for e in $(cat /tmp/datalist.txt)
do
  tail -1 /var/gardisto/$e > /tmp/$(hostname -s)$e
done
#scp file to gardisto host
for a in $(ls /tmp/$(hostname -s)*)
do
  scp /tmp/$a gardisto@$serverfqdn:/var/gardisto/collectors/
done
