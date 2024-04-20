for i in range(10,1,-1):
    print(i)

for i in range(10,1,-5):
    print(i)

import math
from urllib.request import AbstractDigestAuthHandler
print(math.floor(3/2))
print(math.ceil(3/2))

arr=[1,2,3,4,5]
print(arr)
arr.insert(0,-3)
print(arr)
arr[2]=7
print(arr)

a,b,c=[1,2,3]
print(a,b,c)

#zip function
lis1=[1,2,3]
lis2=[4,5,6]
for n1,n2 in zip(lis1,lis2):
    print(n1,n2)

#reverse 
lis1=[1,2,3]
lis1.reverse()
print(lis1)

#list comprehension
arr=[i*i for i in range(5)]
print(arr)

arr=[[0]*3 for i in range(3)]
print(arr)

#string slicing
s="abcd"
print(s[0:2])
print(s[1:4])

s="abcd"
s+="ef"
print(s)

#queues

from collections import deque
queue=deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)

queue.appendleft(5)
print(queue)
queue.append(6)
print(queue)