#!/usr/bin/env python
'''
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
prints out both the MIB2 sysName and sysDescr.
'''

from snmp_helper import snmp_get_oid, snmp_extract

COMMUNITY_STRING = 'galileo'
SNMP_SYSNAME = '1.3.6.1.2.1.1.5.0'
SNMP_SYSDESCR = '1.3.6.1.2.1.1.1.0'


def main():
    '''
    Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2)
    and prints out both the MIB2 sysName and sysDescr.
    '''

    ip_addr = raw_input("IP Address: ")
    ip_addr = ip_addr.strip()

    # set the IP Address, community string, and SNMP Ports per device
    pynet_rtr1 = (ip_addr, COMMUNITY_STRING, 7961)
    pynet_rtr2 = (ip_addr, COMMUNITY_STRING, 8061)

    for device in (pynet_rtr1, pynet_rtr2):
        for oid in (SNMP_SYSNAME, SNMP_SYSDESCR):
            data = snmp_get_oid(device, oid)
            output = snmp_extract(data)

            print output

if __name__ == "__main__":
    main()

