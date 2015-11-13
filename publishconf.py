#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Bad fix to get common confs
import sys
import os
sys.path.append('.')

from pelicanconf import *

STAGINGURL = 'https://staging-brasil-pyladies.herokuapp.com/'
PRODURL = 'https://pyladies-brazil.github.io/br-pyladies-pelican'

SITEURL = STAGINGURL

if "ENV" in os.environ:
  if os.environ['ENV'] == "production":
    SITEURL = PRODURL