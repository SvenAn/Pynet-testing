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

getping = net_connect.send_command("ping", expect_string = r'Protocol')
getping += net_connect.send_command("ip", expect_string = r'Target IP address')
getping += net_connect.send_command("8.8.8.8", expect_string = r'Repeat count')
getping += net_connect.send_command("5", expect_string = r'Datagram size')
getping += net_connect.send_command("100", expect_string = r'Timeout in seconds')
getping += net_connect.send_command("2", expect_string = r'Extended commands')
getping += net_connect.send_command("n", expect_string = r'Sweep range of sizes')
getping += net_connect.send_command("n", expect_string = r'Success rate')

print (getping)

net_connect.disconnect()
