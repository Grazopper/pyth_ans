#!/usr/bin/env python

import telnetlib
import time


def main():
    IP_ADDR = '50.76.53.27'
    TELNET_PORT = 23
    TELNET_TIMEOUT = 6
    USERNAME = 'pyclass'
    PASSWORD = '88newclass'


    remote_conn = telnetlib.Telnet(IP_ADDR, TELNET_PORT, TELNET_TIMEOUT)
    
    output = remote_conn.read_until('sername:', TELNET_TIMEOUT)
    remote_conn.write(USERNAME + '\n')
    output += remote_conn.read_until('assword:', TELNET_TIMEOUT)
    print output
    remote_conn.write(PASSWORD + '\n')
    
    output = remote_conn.read_very_eager()
    print output

    remote_conn.write('show ip int brief' + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output

    remote_conn.close()


if __name__ == "__main__":

    main()
