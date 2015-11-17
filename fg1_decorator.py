__author__ = 'Sawl_Stone'

def limits(a, b):
    def wrapper1(f):
        def wrapper2(*args, **kargs):
            print("wrapper")
            count = args[0]
            per = args[1]
            if (per < a):
                per = a
            if (per > b):
                per = b
            res = f(count, per)
            return res

        return wrapper2
    return wrapper1

@limits(0, 30)
def percents(count, per):
    if(per > 30):
        per = 30
    count = count + count * per / 100
    return count

def main():
    res = percents(300, 100)
    print(res)

main()