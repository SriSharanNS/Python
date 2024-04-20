nums=[1,2,3,4,5,6,7,8,9,10]

list=[]
for i in nums:
    list.append(i*i)
print (list)    

list=[i*i for i in nums]
print(list) 

def cube(i):
    return i*i*i
list1= map(cube, nums)
print(list1)

list2=(filter(lambda i:i%2==0,nums))
print(list2)

