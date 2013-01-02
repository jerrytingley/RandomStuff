from __future__ import division
## Misc functions, mainly math related

# Can be found through:
# phi = (1/2)*(1 + math.sqrt(5)) = (1/2)*(1 + 2.23606797749979)
phi = 1.618033988749895

# Can be estimated through: pi = (9801)/(2*1103*math.sqrt(2))
pi = 3.1415927300133055

# Can be estimated through: (1 + (1/n))**n with high values of n
e = 2.7182820532347876

# Substituted values constant no matter input for there actual values
fib = lambda n: int(((3.23606797749979**n)+(1.2360679774997898**n))/((2**n)*(2.23606797749979)))

# Found this in my math journal, pretty useless.
# Orginally had lim weird_fib as x approached infinity = infinity
weird_fib = lambda x: ((fib(x+2)**2)+(fib(x+1)**2))-((fib(x)**2)+fib(x+1)**2)

# Ramaujan approximation of the factorial function
fact = lambda n: int(((pi**(1/2))*((n/e)**n))*((8*n**3)+(4*n**2)+n+(1/30))**(1/6))

# A q-analog of n has a limit has that function approaches 1, so 0.99
# is used to make it lambda compatiable
q_analog = lambda n: (1-0.99**n)/(1-0.99)

# Simpson rule for approximating a definite integral
simpson = lambda a, b, f: f(a) + 4*f(((a+b)/2))+f(b) * ((b-a)/6)
