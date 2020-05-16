#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass



ciscoswitch1 = { 
    "device_type": "cisco_nxos",
    "host":        "nxos1.lasthop.io",
    "username":    "pyclass",
#    "password":    getpass(),
    "password":    "88newclass",
    "session_log": "session.txt",
#    'fast_cli': True,
}

ciscoswitch2 = { 
    "device_type": "cisco_nxos",
    "host":        "nxos2.lasthop.io",
    "username":    "pyclass",
#    "password":    getpass(),
    "password":    "88newclass",
    "session_log": "session.txt",
#    'fast_cli': True,
}


for switch in ( ciscoswitch1, ciscoswitch2 ):
    net_connect = ConnectHandler( **switch )

    output = net_connect.send_config_from_file( "config.txt" )
    print("\n\n" + output + "\n\n")

    get_save = net_connect.save_config()
    print ("\n\n" + get_save + "\n\n")

    prompt = net_connect.find_prompt()
    print( prompt )

    net_connect.disconnect()
