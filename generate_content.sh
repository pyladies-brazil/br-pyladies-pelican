#!/bin/bash
pelican /app/content -o /app/public -s publishconf.py
chmod 755 /app/public
