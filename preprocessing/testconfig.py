#!/usr/bin/python

import json
with open('pclsearch.json') as config_file:
    config = json.load(config_file)
print config['sources']['conference']['pcsc']['2017']
