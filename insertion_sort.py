def insertion_sort(lis):
    for i in range(1,len(lis)):
        anchor=lis[i]
        j=i-1

        while j>=0 and anchor<lis[j]:
            lis[j+1]=lis[j]
            j=j-1
            lis[j+1]=anchor
   
n=int(input("enter the no of elements = "))
lis=[]
for i in range(n):
    ele=int(input())
    lis.append(ele)
print(lis)
insertion_sort(lis)
print(lis) 