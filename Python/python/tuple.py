my_tuple = (1,2,3)
my_tuple
my_second = (5,)
my_second
my_fourth_tuple = tuple ([1,2,3,])
my_fourth_tuple


def add(base, *args):
    total = base
    for num in args:
        total += num
    return total

add(5, 20)


def multiply(base, *args):
    total = base
    for num in args:
        total *= num
    return total

add(5, 20)



count = 1
for letter in "abcdefghi":
    print("{}: {}".format(count,letter))
    count += 1

def combo(iter1, iter2):
    output = []
    for i in range(0, len(iter1)):
        output += (iter1[i], iter2[i])
    return output


def combo(iter1, iter2):
    output = []
    for i in range(0, len(iter1)):
        output += (iter1[i], iter2[i]),
    return output
