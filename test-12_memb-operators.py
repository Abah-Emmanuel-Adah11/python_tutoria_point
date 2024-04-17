#!/usr/bin/python3

a = 10
b = 20
list = [1, 2, 3, 4, 5]


if ( a in list ):
    print ("Line 1 - a is aialable in the given list")
else:
    print ("Line 1 - a is not avialable in the given list")



if ( b not in list ):
    print ("Line 2 - b is not avialable in the given list")
else:
    print ("Line 2 - b is avialable in the the given list")


#NEXT STEP
c = b/a

if ( c in list ):
    print ("Line 3 - c is avialable in the given list")
else:
    print ("Line 3 - c is not avialable in the given list")


