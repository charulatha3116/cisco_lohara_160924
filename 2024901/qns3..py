list=input('enter the integers').split()
print(list)
t=()
for i in list:
    t+=(i,)
print(t)
s=set(list)
f=frozenset(s)
print(s)
print(f)
dict={key:key*2 for key in f}
print(dict)




