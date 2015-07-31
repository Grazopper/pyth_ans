#!/usr/bin/env python
'''
Using ciscoconfparse find the crypto maps that are not using AES (based-on the
transform set name). Print these entries and their corresponding transform set
name.
'''

from ciscoconfparse import CiscoConfParse

def main():
    '''
    Using ciscoconfparse find the crypto maps that are not using AES (based-on
    the transform set name). Print these entries and their corresponding
    transform set name.
    '''

    # Create a new CiscoConfParse object using our sample config file
    cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

    # Find all entries with children that do NOT have "set transform-set AES-SHA", and a parent of "crypto map CRYPTO"
    crypto = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES-SHA")

    # Loop over the list, printing each object, and it's associated children
    for i in crypto:
        print i.text

        for child in i.children:
            print child.text

if __name__ == "__main__":
    main()

