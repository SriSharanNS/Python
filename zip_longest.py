from itertools import zip_longest
nums1=[1,2,3,4,5,6]
nums2=[11,22,33,44,55,66,77,88,99]
print("".join(a+b for a,b in zip_longest(nums1,nums2,fillvalue="")))