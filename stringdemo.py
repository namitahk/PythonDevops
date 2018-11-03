#!/usr/bin/python   
#This is to create file self executable

myname = "Namita"
print (myname)
print (type(myname))

print (myname.lower())
print (myname.upper())
print (myname.title())
print('\n')
print (len(myname))
print (myname[2])
print( myname[1:])
print (myname[:3])
print ('\n' "Printing Last Char!!!")
print (myname[:-1])
print (myname[:-3])
print ('\n' "Printing Reverse!!!")
print (" -1"+ myname[::-1])
print (" -2"+ myname[::-2])

letter = 'z'
letter = letter*10
print (letter)


splitdemo = "I am Devops Engineer" 
print (splitdemo.split(' ')) 


print('This is a string with an {p}'.format(p='insert'))

# Multiple times:
print('One: {p}, Two: {p}, Three: {p}'.format(p='Hi!'))


# Several Objects:
print('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3))
