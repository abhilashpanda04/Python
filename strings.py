#ordered,immutable and text representation

mystring="hello world"

mystring

mystring_1='i 'm a boy'  #value error

mystring_1='i \'m a boy'

mystring_1="i 'm a boy"
mystring_1

# access the index or charachter of a string

char=mystring[0]
char

#type error
mystring[0]='y'# cannot perform , cnt change a charachter inside a string

substring=mystring[0:4]

substring

# reverse a string

substring=mystring[::-1]

substring

greeting="hello"
name="tom"

text=greeting+" "+name
text

for i in mystring:
    print(i)

if 'h' in mystring:
    print("yes")
else:
    print("No")



mystring="   hello world   "

mystring_1=mystring.strip()

mystring_1


# the below function does not change the origional string rather gives a new string

mystring_1.upper()

mystring_1.lower()

mystring.startswith('')

mystring.endswith('world')

mystring.find('o')

mystring.count('o')

mystring.replace('world','tune')

mystring

#split with the deliemiter

mystring="how are you doing"

mylist=mystring.split(" ")

mylist

# add an additional space or , to the list or string

new_string=" ".join(mylist)

new_string

list=['a']*8

list
from timeit import default_timer as timer
mystring= ''

start=timer()
for i in list:
    mystring+=i
    end=timer()
    print(start-end)



var=123

my_string="the digit is %d", %var

my_string

var1=2.133444
var2=76

my_string="the digit is {:.2f} and {}".format(var1,var2)

my_string

my_string=f"the digit is {var1} and {var2}"

my_string

my_string=f"the digit is {var1*4} and {var2}"

my_string
