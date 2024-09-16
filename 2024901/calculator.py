def cal(first:int,second:int)->int:
    sum=first+second
    diff=first-second
    product=first*second
    quotient=first//second
    return sum,diff,product,quotient


s,d,p,q=cal(20,6)
print(s,d,p,q)

t1=cal(10,6)
print(t1)
print(type(t1))