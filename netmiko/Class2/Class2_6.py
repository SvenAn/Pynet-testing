#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass
from time import sleep


#password = getpass()
password = "88newclass"

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
    'fast_cli': True,
}
net_connect = ConnectHandler( **device )


# a.
def get_prompt():
    prompt = net_connect.find_prompt()
    print( "prompt: " + prompt)

print("a.")
get_prompt()


# b.
print("\nb.")
net_connect.config_mode()
get_prompt()


# c.
print("\nc.")
net_connect.exit_config_mode()
get_prompt()


# d.
print("\nd.")
net_connect.write_channel("disable\n")


# e.
print("\ne.")
sleep(2)
my_read = net_connect.read_channel()
print(my_read)


# f.
print("\nf.")
net_connect.enable()
get_prompt()









net_connect.disconnect()
