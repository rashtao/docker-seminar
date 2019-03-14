#!/usr/bin/env python

import sys
import time
from pytime import pytime


# print args
print('Number of arguments:', len(sys.argv), 'arguments')
print('Argument List:', str(sys.argv))


year = 2000
while True:

    # calculate Easter day for current year
    easter_date = pytime.easter(year)
    log = "In " + str(year) + " Easter is on " + str(easter_date)

    print(log)

    time.sleep(1)
    year = year + 1

    # exit after 2 minutes
    if year > 2120:
        break
