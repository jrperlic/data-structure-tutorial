from collections import deque

def mystery1(ll):
    for i in reversed(ll):
        print(i, end=" ")
    print("")

def mystery2(ll):
    for i in range(0, len(ll), 2):
        print(ll[i], end=" ")
    for i in range(1, len(ll), 2):
        print(ll[i], end=" ")


ll = deque([1, 2, 3, 4, 5])

mystery1(ll) # 5 4 3 2 1
mystery2(ll) # 1 3 5 2 4