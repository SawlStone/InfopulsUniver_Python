__author__ = 'Sawl_Stone'


# insert-sort
def min(massive, start):
    minElem = massive[start]
    index = start
    for i in range(start, len(massive)):
        if minElem > massive[i]:
            minElem = massive[i]
            index = i
    return index

def swap(i, j, massive):
    massive[i], massive[j] = massive[j], massive[i]

def insertSort(massive):
    for i in range(0 , len(massive)):
        index = min(massive, i)
        swap(i, index, massive)
    return massive

def main():
    mas = [10, 30, 20, 69, 45, 90, 100]
    print(mas)
    insertSort(mas)
    print(mas)

main()
