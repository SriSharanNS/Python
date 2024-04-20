def selection_sort(lis):

    size=len(lis)

    for i in range(size-1):
        min_index=i
        for j in range(min_index+1,size):
            if lis[j]<lis[min_index]:
                min_index=j
        #if i!=min_index:
                lis[i],lis[min_index]=lis[min_index],lis[i]        


n=int(input("enter the no of elements = "))
lis=[]
for i in range(n):
    ele=int(input())
    lis.append(ele)
print(lis)
selection_sort(lis)
print(lis)
