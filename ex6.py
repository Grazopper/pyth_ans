#!/usr/bin/env python
'''
Write a Python program that creates a list. One of the elements of the list
should be a dictionary with at least two keys. Write this list out to a file
using both YAML and JSON formats. The YAML file should be in the expanded form.
'''

import yaml
import json

def main():
    '''
    Write a Python program that creates a list. One of the elements of the list
    should be a dictionary with at least two keys. Write this list out to a file
    using both YAML and JSON formats. The YAML file should be in the expanded form.
    '''   
    # Create a list of items, including dictionary key/values
    test_list = range(10)
    test_list.append('Some text')
    test_list.append('Bugaboo')
    test_list.append({})
    test_list[-1]['fruit'] = 'orange'
    test_list[-1]['veggie'] = 'carrot'
    test_list[-1]['dict'] = 'ionary'

    #  Dump the yaml list using the expanded form
    yaml.dump(test_list, default_flow_style=False)

    # Save the yaml dump to a file
    with open("test_file.yml", "w") as f:
        f.write(yaml.dump(test_list, default_flow_style=False))


    #  Dump the json list
    json.dumps(test_list)

    # Save the json dump to a file
    with open("test_file.json", "w") as f:
        json.dump(test_list, f)

if __name__ == "__main__":
    main()
