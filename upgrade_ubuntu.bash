#!/bin/bash

# Update the system
sudo apt-get update -y

# Upgrade installed packages
sudo apt-get upgrade -y

# The below command will perform upgrades involving changing dependencies, 
# adding or removing new packages as necessary
sudo apt-get dist-upgrade -y

# Make sure you have the update-manager-core package installed
sudo apt-get install update-manager-core -y

# Upgrade to any latest release
sudo do-release-upgrade
