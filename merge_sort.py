def merge_sort(res_arr):
    if len(res_arr)>1:

            left_arr=res_arr[:len(res_arr)//2]
            right_arr=res_arr[len(res_arr)//2:]


            merge_sort(left_arr)
            merge_sort(right_arr)

            i=0
            j=0
            k=0
            
            while i<len(left_arr) and j<len(right_arr):
                if left_arr[i]<right_arr[j]:
                    res_arr[k]=left_arr[i]
                    i+=1
                else:
                    res_arr[k]=right_arr[j]
                    j+=1

                k+=1


            while i<len(left_arr):
                res_arr[k]=left_arr[i]
                i+=1
                k+=1

            while j<len(right_arr):
                res_arr[k]=right_arr[j]
                j+=1
                k+=1

res_arr=[]
n=int(input("enter the number of elements = "))
for i in range(n):
    ele=int(input())
    res_arr.append(ele)
print(res_arr)
merge_sort(res_arr) 
print(res_arr)   

