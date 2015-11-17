__author__ = 'Sawl_Stone'

def hanoy(n, a, b, c):
    if n > 0:
        hanoy(n-1, a, c, b)
        print("we put disk " + str(n) + " from " + a +" to " + c)
        hanoy(n-1, b, a, c)

def main():
    hanoy(3, 'a', 'b', 'c')

main()