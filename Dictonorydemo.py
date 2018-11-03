#!/usr/bin/python


# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}
print (my_dict)

print (my_dict['key2'])
print (my_dict.keys())
print (my_dict.values())
print (my_dict.items())


for k,v in my_dict.items():
  print k
  print v
