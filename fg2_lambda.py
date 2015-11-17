__author__ = 'Sawl_Stone'

"""
def main():
    func = lambda x: x+1
    res = func(10)
    print(res)

main()
"""

def operation(a, b, f):
    return f(a, b)

def main():
    res = operation(20, 30, lambda c, d: if(c>d) else d)
    print(res)

main()
