from ciscoconfparse import CiscoConfParse

# Create a new CiscoConfParse object using our sample config file
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

# Find all entries beginning with crypto map CRYPTO
crypto = cisco_cfg.find_objects(r"^crypto map CRYPTO")

# Loop over the list, printing each object, and it's associated children
for i in crypto:
    print i.text
    
    for child in i.children:
        print child.text
