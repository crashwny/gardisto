#!/usr/bin/env bash
# calls home to enter host into Gardisto database for monitoring

serverFQDN=$(cat /var/gardisto/gardisto.conf |grep SERVER_FQDN|sed 's/SERVER_FQDN='//)

hostData='{}'

data1=$(hostname -s)
data2=$(hostname -i)
data3=$(hostname -f)
data4="SITENAME"
data5="none"

echo "{
            \"toDo\": \"addhost\",
            \"hostname\": \""$data1",
            \"ip\": \""$data2"\",
            \"fqdn\": \""$data3"\",
            \"site\": \""$data4"\",
            \"hostType\": \"\",
            \"parent\": \"\",
            \"gardistoAdded\": \"0\",
            \"gardistoKeyAdded\": \"0\",
            \"userAdded\": \"0\",
            \"userKeyAdded\": \"0\",
            \"snooze\": \"0\"
        }">/tmp/garadd-$data1.json

scp /tmp/garadd-$data1.json gardisto@$serverFQDN:/tmp/
ssh gardisto@$serverFQDN "gardisto scriptEntry"

#class Host:
#    def __init__(self):
#        details = dict({
#            "toDo": "",
#            "hostname": "",
#            "ip": "",
#            "fqdn": "",
#            "site": "",
#            "hostType": "",
#            "parent": "",
#            "gardistoAdded": "0",
#            "gardistoKeyAdded": "0",
#            "userAdded": "0",
#            "userKeyAdded": "0",
#            "snooze": "0"
#            })
