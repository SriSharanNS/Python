nums=[1,2,3,4,5,6,7,8,9,10]

def cube(i):
    return i*i*i
list1= map(cube, nums)
print(list(list1))

list2=(filter(lambda i:i%2==0,nums))
print(list(list2))