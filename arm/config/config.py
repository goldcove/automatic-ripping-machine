#!/usr/bin/python3

import os
# import re
import yaml

yamlfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/etc/arm", "arm.yaml")

with open(yamlfile, "r") as f:
    cfg = yaml.load(f)
