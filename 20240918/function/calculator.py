def find_sum(first:int=1,second:int=3)->int:
    return first+second
    
print(find_sum(10,20))
print(find_sum(second=10,first=20))
print(find_sum(second=30))
print(find_sum())
print(type(find_sum))


"""def change_names(names,index,name):
    names[index]=name
names=['rahul','modi']
print(names)
change_names(names,1,'cbn')
print(names)

print(sum([10,20,30]))

def find_diff(first,second,*others):
    s=first-second
    if(len(others)>0):
        for num in others:
            s+=num
        #end for
    #print(type(others))
    return s
print(find_diff(30,10))
print(find_diff(30,10,5))
print(find_diff(30,10,5,2,1))"""


"""def find_diff(first,second,**others):
    s=first-second
    if(len(others)>0):
        for key in others:
            s+=others[key]
        #end for
    #end if
    #print(type(others))
    return sd
print(find_diff(first=30,second=10))
print(find_diff(first=30,second=10,third=5))
print(find_diff(first=30,second=10,third=5,fourth=2,fifth=1))"""

"""def fact(N):
    if N<=1:#base/edge case condition
        return 1
    return N*fact(N-1)

print(fact(5))
print(fact(4))"""

import math
def is_prime(N):
    N_sqrt = int(math.sqrt(N))
    for i in range(2,N_sqrt+1):
        if N%i==0:
            return False
        
    return True

print(is_prime(5))
print(is_prime(51))
print(is_prime(60))
print(is_prime(61))