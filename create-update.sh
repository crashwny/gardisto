#!/usr/bin/env bash
# create an update package for satellites 0.2.2 to 0.2.3

mkdir -p /tmp/update-package/collectors
cp ~/gardisto/collectors/* /tmp/update-package/collectors/
cp /var/gardisto/gardisto.conf /tmp/update-package/
cd /tmp/
tar -czf /var/gardisto/update-package.tar.gz update-package
