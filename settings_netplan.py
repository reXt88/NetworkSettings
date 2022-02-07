#!/bin/python3
import os
import os.path

with open("/etc/netplan/00-installer-config.yaml", "w") as f:
	f.write('''network:
  ethernets:
    enp0s3:
      dhcp4: yes
    enp0s8:
      dhcp4: yes
  version: 2''')
os.system("netplan apply")
