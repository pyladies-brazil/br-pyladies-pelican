#!/bin/bash
/app/.heroku/python/bin/pelican /app/content -o /app/public -s /app/publishconf.py

# check for a good exit
if [ $? -ne 0 ]
then
	  # something went wrong; convey that and exit
	    exit 1
fi

chmod 755 /app/public
