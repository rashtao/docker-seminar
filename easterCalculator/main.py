import time
from pytime import pytime

year = 2000

while True:

    easter_date = pytime.easter(year)
    log = "In " + str(year) + " Easter is on " + str(easter_date)

    print(log)

    time.sleep(1)
    year = year + 1
