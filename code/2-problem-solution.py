from collections import deque

n = int(input())
ll = deque(list(map(int, input().split())))
stack = []

for i in range(n):
   if not ll[i] % 2:
       stack.append(ll[i])
       continue
   else:
       if stack:
           while stack:
               print(stack.pop(), end=" ")
       else:
           print(ll[i], end=" ")
           continue
       print(ll[i], end=" ")

if stack:
   while stack:
       print(stack.pop(), end=" ")