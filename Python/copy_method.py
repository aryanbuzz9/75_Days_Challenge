#1st assignment method
a=[1,2,3,4]
b=a
# print(a)
b[1]=99
# print(b)
# print(a)

#copy
# import  
x=[1,2,3,4,5]
# y=x.copy()
# print(x)
# print(y)
# y[1]=100
# print(x,y)

import copy

u=[[10,20],[30,40]]
v=copy.copy(u)
print(v)

v[1][0]=100
print(u,v)

m=[[10,20],[30,40]]
n=copy.deepcopy(m)
print(m)

n[1][0]=100
print(m,n)



