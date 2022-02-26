#!/bin/bash
printf 'Enabled logging...'
sudo sed -i 's/#general_log/general_log/g' /etc/mysql/my.cnf
printf '\nRestarting MySQL...'
sudo systemctl restart mysql
printf '\nTailing MySQL logs...\n'
sleep 10
sudo tail -f /var/log/mysql/mysql.log