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

ciscoswitch2 = { 
    "device_type": "cisco_ios",
    "host":        "cisco4.lasthop.io",
    "username":    "pyclass",
    "password":    password,
    "session_log": "session.txt",
}

for switch in ( ciscoswitch1, ciscoswitch2 ):
    net_connect = ConnectHandler( **switch )
    print( net_connect.find_prompt() )


net_connect.disconnect()
