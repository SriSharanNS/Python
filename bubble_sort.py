def bubble_sort(lis):

    size=len(lis)

    for i in range(size-1):
        swapped=False
        for j in range(size-1-i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
                swapped=True

        if not swapped :
            break;            


n=int(input("enter the size of list = "))

lis=[]

for i in range(n):

    ele=int(input())
    lis.append(ele)

print(lis)

bubble_sort(lis)

print(lis)
