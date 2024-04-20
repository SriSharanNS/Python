n=int(input("enter the size of array = "))

arr=[]

for i in range(n):

    ele=int(input())
    arr.append(ele)
    
print(arr)    


def max_heapify(arr,n,i):

    largest=i
    left=2*i + 1
    right=2*i + 2

    if left<n and arr[largest]<arr[left]:

        largest=left

    if right<n and arr[largest]<arr[right]:

        largest=right

    if largest!=i:

        arr[i],arr[largest]=arr[largest],arr[i]

        max_heapify(arr,n,largest)           


def heap_sort(arr):

    for i in range(n-1,0,-1):

        arr[i],arr[0]=arr[0],arr[i]
        max_heapify(arr,i,0)

for i in range(n//2-1,-1,-1):

    max_heapify(arr,n,i)

heap_sort(arr)    


print("sorted array is ") 
print(arr)   