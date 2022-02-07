#!/bin/python3
import os.path
import os

print("static or dynamic")
print("   1         2")
a = input()
if a == "2"
with open("/etc/network/interfaces", "w") as f:
	f.write('''auto enp0s3
iface enp0s3 inet dhcp

auto enp0s8
iface enp0s8 inet dhcp''')
elif a == "1":
	devices = input("How many interfaces do you have ")
	if devices == "1":
		addr1 = input("Enter address for enp0s3 ")
		netmask1 = input("Enter netmask for enp0s3 ")
		with open ("/etc/network/interfaces", "w") as f:
			f.write(f'''auto eth0
iface eth0 inet static
	address {addr1}
	netmask {netmask1}''')
	if devices == "2":
		addr1 = input("Enter address for enp0s3 ")
                netmask1 = input("Enter netmask for enp0s3 ")
		addr2 = input("Enter address for enp0s8 ")
                netmask2 = input("Enter netmask for enp0s8 ")
		with open ("/etc/network/interfaces", "w") as f:
			f.write(f'''auto enp0s3
iface enp0s3 inet static
	address {addr1}
	netmask {netmask1}
auto enp0s8
iface enp0s8 inet static
        address {addr2}
        netmask {netmask2}''')
os.system("systemctl restart networking.service")
