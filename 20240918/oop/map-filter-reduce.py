from functools import reduce

nums=[2,3,4]
#map-syntax
#map(<func>,iterable)
nums_sqr=list(map(lambda num:num**2,nums))
print(nums_sqr)

nums_even=filter(lambda num:num%2==0,nums)
print(nums_even) 

import sys
nums=[10,20,30,41]
nums_sum=reduce(lambda s,num:s+num,nums,0)
nums_prod=reduce(lambda p,num:p*num,nums,1)
nums_max=reduce(lambda m,num:max(m,num),nums,sys.maxsize)
nums_min=reduce(lambda m,num:min(m,num),nums,-sys.maxsize)
print(nums_sum)
print(nums_prod)
print(nums_max)
print(nums_min)


nums_max=reduce(max,nums)
nums_min=reduce(min,nums)

print(nums_max,nums_min)