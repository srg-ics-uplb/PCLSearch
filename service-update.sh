#!/bin/bash
sudo docker-compose stop $1
sudo docker-compose build $1
sudo docker-compose start $1
