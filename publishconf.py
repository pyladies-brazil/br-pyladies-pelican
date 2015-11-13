#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Bad fix to get common confs
import sys
import os
sys.path.append('.')

from pelicanconf import *

STAGINGURL = 'https://staging-brasil-pyladies.herokuapp.com/'
PRODURL = 'https://pyladies-brazil.github.io/br-pyladies-pelican'

if os.environ['ENV'] == "production":
    print "prod"
    SITEURL = PRODURL
else:
    print "else"
    SITEURL = STAGINGURL
