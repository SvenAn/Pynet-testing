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

get_version = net_connect.send_command("show version", use_textfsm=True)
print (get_version)

get_lldp = net_connect.send_command("show lldp neighbors", use_textfsm=True)
print ("Neigbor if: " + get_lldp[0]['neighbor_interface'])

net_connect.disconnect()
