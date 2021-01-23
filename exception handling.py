#syntax error happens when the parser detect something syntactical wrong

#exception error happend  when
#TypeError # number and string

a=5 + 'Ten'
#ImportError

import abhilash

#mudulenot found error
#name error

a=5
b=c
#file not found error

f=open("somefile.txt")
#value error

a=[1,2,3]
a.remove(1)

a

a.remove(7)
#index error

a[7]
#key error

mydict={'name':'max'}

mydict["age"]


x=5

if x<0:
    raise Exception('x should be positive')


x=-5

assert(x<=0),'x is not negetive'

a=5 / 0

try:
    a= 5/0
except:
    print("error has happened")


try:
    a= 5/0
except Exception as e:
    print(e)

try:
    a= 5 / 1
    b=a + 4
except ZeroDivisionError as e :
    print(e)
except TypeError as e:
    print(e)
else:
    print("everything is fine")
finally:
    print('clean')
class ValueTooHigh(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHigh("value is too high")

    test_value(200)


class ValueTooHigh(Exception):
    pass
class ValueTooSmall(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value

    

def test_value(x):
    if x > 100:
        raise ValueTooHigh("value is too high")
    if x<5:
        raise ValueTooSmall("value is too small",x)
try:
    test_value(1)
except ValueTooHigh as e:
    print(e)
except ValueTooSmall as e:
    print(e.message,e.value)
