#!/usr/bin/python
import pdb

my_list = [1,2,3]
#pdb.set_trace()
print (my_list)
print (my_list * 2)

print ('\n' "Append list func")
l = [1,2,3]
l.append('append me!')
print(l)
l.pop(0)
print(l)


print ('\n' "Iterate list")
cat_list = ["not eating", "not playing", "on a bed", "is sleeping"]

for state in cat_list:
  print("This cat is " + state)


print ('\n' "Concatenate & sort")
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers_in_order = sorted(numbers)

print(numbers)
print(numbers_in_order)
