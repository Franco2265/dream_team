import random

list = []
for i in range(15) :
    list.append(random.randint(0, 100))

def bogosort(list : list) -> list :
    size = len(list) - 1
    while not issort(list) :
        el1 = random.randint(0, size)
        el2 = random.randint(0, size)
        list[el1], list[el2] = list[el2], list[el1]
    return list

def issort(list) -> bool :
    for i in range(len(list) - 1) :
        if list[i] > list[i + 1] : return False
    return True

print(bogosort(list))