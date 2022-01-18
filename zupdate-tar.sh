#!/usr/bin/env bash

cd ~/gardisto

git archive -o latest.tar.gz HEAD

cp latest.tar.gz ~/gardisto.org/html/

scp -r /home/patrick/gardisto.org/html/latest.tar.gz root@gardisto.org:/tmp

ssh root@gardisto.org "yes | cp /tmp/latest.tar.gz /var/www/html/"
