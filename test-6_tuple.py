#!/usr/bin/python3

tuple = ( 'abcd' , 786 , 2.23, 'john', 70.2 )

tinytuple = (123, 'john')

print (tuple)       # print complete tuple

print (tuple[0])    # print first element of tuple

print (tuple[1:3])  # prints elements starting from 2rd till 3rd

print (tuple[2:])   # print elements starting from 3rd elements

print (tinytuple * 2) # print tinytuple two times


print (tuple + tinytuple) # print concatinated tuple

#The following code is invalid because we attempted to update a tuple, which is not allowed with tuple but is acceptable in list. Let's illustrate using the example below

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]

tuple[2] = 1000 # Invalid syntax with tuple

tuple[2] = 1000 # valid sytax with list


