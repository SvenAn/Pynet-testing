#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass


password = getpass()


ciscoswitch1 = { 
    "device_type": "cisco_ios",
    "host":        "cisco3.lasthop.io",
    "username":    "pyclass",
    "password":    password,
    "session_log": "session.txt",
}

net_connect = ConnectHandler( **ciscoswitch1 )
#print( net_connect.find_prompt() )
version = net_connect.send_command("show version")

file = open('switchversion.txt', 'w')
file.write( version )
file.close()

net_connect.disconnect()
