#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime, timedelta

print ( "Starting Clock.." )
start = datetime.now()


ciscoswitch1 = { 
    "device_type": "cisco_ios",
    "host":        "cisco3.lasthop.io",
    "username":    "pyclass",
#    "password":    getpass(),
    "password":    "88newclass",
#    "session_log": "session.txt",
#    'fast_cli': True,

}

net_connect = ConnectHandler( **ciscoswitch1 )

cfg = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup',
]

output = net_connect.send_config_set( cfg )
print(output)

get_ping = net_connect.send_command("ping google.com")
print (get_ping)

stop = datetime.now()
print( "Duration: ", str( stop - start ) )


net_connect.disconnect()
