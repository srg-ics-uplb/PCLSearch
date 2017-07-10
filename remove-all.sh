#/bin/bash
sudo docker rm $(sudo docker ps -a | grep pclsearch_ | awk '{ print $1 }')
