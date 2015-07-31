from ciscoconfparse import CiscoConfParse

# Create a new CiscoConfParse object using our sample config file
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

# Find all entries with children that have "set pfs group2", and a parent of "crypto map CRYPTO"
crypto = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

# Loop over the list, printing each object, and it's associated children
for i in crypto:
    print i.text

    for child in i.children:
        print child.text




