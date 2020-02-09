import itertools
import time
import sys
colors = ['green', 'yellow', 'red','blue','violet','white','silver','gold']
color = itertools.cycle(colors)
while True:
    sys.stdout.write('\r' + next(color))
    sys.stdout.flush()
    time.sleep(.5)

    