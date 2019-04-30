from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios',
    "session_log": 'my_session.txt'
 }

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = "delete bootflash:/test_file.txt"

output = net_connect.send_command_timing(command, 
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("", 
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("y",
    strip_prompt=False, strip_command=False)

print(output)


