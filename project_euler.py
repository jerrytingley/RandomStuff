def problem_1():
    s = 0
    for x in range(0, 1000): if (x % 3) == 0 or (x % 5) == 0: s += x
    return s

def problem_2():
    fib = lambda n: int(((3.23606797749979**n)+(1.2360679774997898**n))/((2**n)*(2.23606797749979)))
    s = x = 0
    while fib(x) < 4000000:
        if (fib(x) % 2) == 0:
            s += fib(x)
            x+=1
    return s

def problem_3(n):
    k = 2
    while(k * k <= n):
    	if (n % k == 0): n = n / k
    	else: k += 1
    return n

def problem_4():
    a = b = 999
    for x in range(999, 100, -1):
        if str(999*x) == str(999*x)[::-1]:
            return (999, x)
    return -1
