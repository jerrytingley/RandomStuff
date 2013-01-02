from __future__ import division

even = lambda x: True if (x % 2) == 0 else False

def three_n_plus_one(n):
    i = 0
    while n != 1:
        if even(n): n = int(n / 2)
        else: n = int((3 * n) + 1)
        i += 1
        print "[",i,"]", " n = ", n

print three_n_plus_one(22)
