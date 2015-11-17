__author__ = 'Sawl_Stone'

# factorialis

def f(n):
    if n > 1:
        return f(n-1)*n
    else:
        return 1

def main():
    res = f(10)
    print(res)

main()

import math
print(math.factorial(10))
