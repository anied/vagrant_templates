#!/usr/bin/env bash

apt-get update
apt-get install -y apache2
if ! [ -L /var/www/html ]; then
  rm -rf /var/www/html
  ln -fs /vagrant/src /var/www/html
fi

sudo chown 666 /etc/apache2/apache2.conf

# echo "##############################"
# echo "##############################"
# echo ""
# echo "pwd:"
# pwd
# echo "ls"
# ls

echo "*** running python scripts ***"
python /vagrant/enable_apache_overrides.py

sudo chown 644 /etc/apache2/apache2.conf
sudo a2enmod rewrite
sudo service apache2 restart