#!/bin/sh

#run the upgrade & download pip
apt-get update && apt-get install pip


#install the requirements.txt file
apt install -r requirements.txt
