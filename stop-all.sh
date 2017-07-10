#/bin/bash
sudo docker stop $(sudo docker ps -a | grep pclsearch_ | awk '{ print $1 }')
