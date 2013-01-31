from __future__ import division
from math import log

py   = lambda r, ra, e: (r**e)/((r**e)+(ra**e))
exp  = lambda r, ra, g: 1.50 * log((r+ra)/(g)) + 0.45
exp2 = lambda r, ra, g: ((r+ra)/(g))**.287
