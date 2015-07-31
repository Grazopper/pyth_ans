#!/usr/bin/env python
'''
Write a Python program using ciscoconfparse that parses the 'cisco_ipsec.txt'
config file. Note, this config file is not fully valid (i.e. parts of the
configuration are missing).
The script should find all of the crypto map entries in the file (lines that
begin with 'crypto map CRYPTO') and print out the children of each crypto map.
'''

from ciscoconfparse import CiscoConfParse

def main():
    '''
    Find all of the crypto map entries in the file (lines that begin with
    'crypto map CRYPTO') and print out the children of each crypto map.
    '''

    # Create a new CiscoConfParse object using our sample config file
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

    # Find all entries beginning with crypto map CRYPTO
    crypto = cisco_cfg.find_objects(r"^crypto map CRYPTO")

    # Loop over the list, printing each object, and it's associated children
    for i in crypto:
        print i.text
    
        for child in i.children:
            print child.text

if __name__ == "__main__":
    main()

