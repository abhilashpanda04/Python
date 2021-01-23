
#lambda argument:expression

add10= lambda x:x+10

add10(5)

def add_func_10(x):
    return x+10

add_func_10(5)

multiple=lambda x,y:x*y

multiple(6,19)


points2d=[(1,2),(2,3),(3,6),(16,27),(10,28)]

points2d_sorted=sorted(points2d)

points2d_sorted


points2d_sorted=sorted(points2d,key=lambda x:x[1])

points2d_sorted

points2d_sorted=sorted(points2d,key=lambda x:x[0]+x[1])

points2d_sorted


#map(function,seq)

a=[1,2,3,4,5]
b=map(lambda x:x*2,a)

list(b)


#list comprehension
# expressiom then argument
c=[x*2 for x in a]

c

#filter function

#filter(func,seq)

b=filter(lambda x:x%2==0,a)
list(b)

c=[x for x in a if x%2==0]

c

#reduce(function,)
from functools import reduce

producta=reduce(lambda x,y:x*y,a)

producta
