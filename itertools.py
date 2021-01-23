from itertools import product

a=[1,2]
b=[3,4]

#Cartisean product

comb=product(a,b)

list(comb)

comb=product(a,b,repeat=2)
list(comb)

from itertools import permutations

a=[1,2,3]

perm=permutations(a)

list(perm)

#shorter permutations
perm=permutations(a,2)

list(perm)


#length is mendatory in combinations
from itertools import combinations

a=[1,2,3,4]
comb=combinations(a,3)
list(comb)

from itertools import combinations_with_replacement


a=[1,2,3,4]
comb=combinations_with_replacement(a,3)
list(comb)

from itertools import accumulate

a=[1,2,3,4,5]

accu=accumulate(a)

list(accu)


import operator

accu=accumulate(a,func=operator.mul)

list(accu)

a=[1,2,5,4,3]
accu=accumulate(a,func=max)
list(accu)
