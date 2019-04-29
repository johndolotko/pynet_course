#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios'
    }

device2= {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios'
    }

for loop in (device1, device2):
    net_connect = ConnectHandler(**loop)

    print(net_connect.find_prompt())

