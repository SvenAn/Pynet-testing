#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime, timedelta



password = getpass()


ciscoswitch1 = { 
    "device_type": "cisco_nxos",
    "host":        "nxos1.lasthop.io",
    "username":    "pyclass",
    "password":    password,
    "session_log": "session.txt",
    "global_delay_factor": 2,
}

net_connect = ConnectHandler( **ciscoswitch1 )

print ( "First run, using global_delay_factor = 2" )
start = datetime.now()
getlldp = net_connect.send_command( "show lldp neighbors detail" )
# print( getlldp )
stop = datetime.now()

print( "\tDuration: ", str( stop - start ) )


print ( "Second run, using  local delay_factor = 8" )
start = datetime.now()
getlldp = net_connect.send_command( "show lldp neighbors detail", delay_factor = 8 )
# print( getlldp )
stop = datetime.now()

print( "\tDuration: ", str( stop - start ) )


net_connect.disconnect()
