list=[1,2,3,4]

it = iter(list)     # this builds an iterator object

print (next(it))    # print next available element in iterator. Iterator object can be traversed using regular fo statement

#!usr/bin/python3

for x in it:
    print (x, end=" ")
or using next() function
while True:
    try:
        print (next(it))

    except StopIteration:
        sys.exit() # you have to import sys module for this
