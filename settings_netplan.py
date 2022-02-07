#!/bin/python3
import os
import os.path

print("static or dynamic?")
print("   1         2")
a = input()
if a == 2:
	with open("/etc/netplan/00-installer-config.yaml", "w") as f:
		f.write('''network:
  ethernets:
    enp0s3:
      dhcp4: yes
    enp0s8:
      dhcp4: yes
  version: 2''')
elif a == 1:
	devices = input("How many devices do you have ")
	if devices == 1:
		addr1 = input("Enter address for enp0s3 ")
		with open ("/etc/netplan/00-insaller-config.yaml", "w") as f:
			f.write(f'''network:
  ethernets:
    enp0s3:
      dhcp4: no
      addresses: [{addr1}]
''')
	if devices == 2:
		addr1 = input("Enter address for enp0s3 ")
		addr2 = input("Enter address for enp0s8 ")
	with open("/etc/netplan/00-installer-config.yaml", "w") as f:
		f.write(f'''network:
  ethernets:
    enp0s3:
      dhcp4: no
      addresses: [{aadr1}]
    enp0s9:
      dhcp4: no
      addresses: [{addr2}]''')
os.system("netplan apply")
