from collections import Counter
a="aaaabbbcccccc"
my_counter=Counter(a)
my_counter

my_counter.keys()

my_counter.values()

my_counter.items()

my_counter.most_common(2)

my_counter.most_common(2)[0]

print(my_counter.elements())

from collections import namedtuple

point=namedtuple('Point','x,y')

pt=point(2,3)

pt.x

pt.y

from collections import OrderedDict

ordered_dict=OrderedDict()

ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=12
ordered_dict['d']=3
ordered_dict['e']=4
ordered_dict['f']=7

ordered_dict
from collections import defaultdict

d=defaultdict(int)
d=defaultdict(float)
d['a']=1
d['b']=2
d['c']=2
d['d']=3

d['e']

from collections import deque
d=deque()

# a data structure where data can be added from left and right
d.append(2)
d.append(3)
d

d.appendleft(4)
d


#remove the last element

d.pop()
d

d.popleft()
d

d.clear()

d.extend([4,5,6])
d

d.extendleft([7,9,8.6])

d

d.rotate(1)
d

d.rotate(2)
d

d.rotate(-2)
d
