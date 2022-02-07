#!/bin/python3
import os.path
import os


with open("/etc/network/interfaces", "w") as f:
	f.write('''auto enp0s3
iface enp0s3 inet dhcp

auto enp0s8
iface enp0s8 inet dhcp''')

os.system("systemctl restart networking.service")
