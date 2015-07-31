#!/usr/bin/env python
'''
Write a Python program that reads both the YAML file and the JSON file created
in exercise6 and pretty prints the data structure that is returned.
'''

import yaml
import json

from pprint import pprint as pp

def main():
    '''
    Write a Python program that reads both the YAML file and the JSON file created
    in exercise6 and pretty prints the data structure that is returned.
    '''

    # Read yaml file
    with open("test_file.yml") as f:
        yaml_list = yaml.load(f)

    # Pretty print yaml
    for y in yaml_list:
        pp(y)

    # Read json file
    with open("test_file.json") as f:
        json_list = json.load(f)

    # Pretty print json
    for j in json_list:
        pp(j)

if __name__ == "__main__":
    main()

