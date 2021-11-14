
from itertools import permutations


def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

x = "" #type a text here

x = Convert(x)

while 1:

    x = Convert(str(list(permutations(x, len(x)))))
