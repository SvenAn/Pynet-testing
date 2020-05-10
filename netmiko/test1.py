#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass

exos_test = ConnectHandler(
    device_type="extreme",
    host="10.202.102.222",
    username="netmiko",
    password=getpass(),
    session_log="session.txt",
)

output = net_connect.send_command("show ports no-refresh")
print(output)

net_connect.disconnect()
