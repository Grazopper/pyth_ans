
#!/usr/bin/env python
'''
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6


class Connection(object):

    ''' A class to initiate a telnet connection, and then issue a command. '''

    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

        try:
            self.remote_conn = telnetlib.Telnet(
                ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except:
            sys.exit("Connection timed out")

    def login(self):
        ''' Login to the network device. '''

        output = self.remote_conn.read_until("sername:", TELNET_TIMEOUT)
        self.remote_conn.write(self.username + '\n')
        output += self.remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        self.remote_conn.write(self.password + '\n')
        time.sleep(1)
        return output

    def send_command(self, cmd="\n"):
        ''' Send a command to the network device. '''

        cmd = cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(1)
        return self.remote_conn.read_very_eager()

    def disable_paging(self, paging_cmd='terminal length 0'):
        ''' Disable the paging of output (i.e. --More--). '''

        return self.send_command(paging_cmd)

    def close_connection(self):
        ''' Close the telnet connection. '''

        self.remote_conn.close()


def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes
    the 'show ip int brief' command.
    '''

    ip_addr = raw_input("IP Address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()

    new_connection = Connection(ip_addr, username, password)
    new_connection.login()
    new_connection.send_command()
    new_connection.disable_paging()
    output = new_connection.send_command('show ip int brief')

    print output
    new_connection.close_connection()


if __name__ == "__main__":
    main()

