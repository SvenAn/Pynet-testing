#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass


password = getpass()


ciscoswitch1 = { 
    "device_type": "cisco_ios",
    "host":        "cisco4.lasthop.io",
    "username":    "pyclass",
    "password":    password,
    "session_log": "session.txt",
}

net_connect = ConnectHandler( **ciscoswitch1 )

getping = net_connect.send_command_timing("ping")
getping += net_connect.send_command_timing("ip")
getping += net_connect.send_command_timing("8.8.8.8")
getping += net_connect.send_command_timing("5")
getping += net_connect.send_command_timing("100")
getping += net_connect.send_command_timing("2")
getping += net_connect.send_command_timing("n")
getping += net_connect.send_command_timing("n")

print (getping)

net_connect.disconnect()
