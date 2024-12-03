# list can have elements of different data type.
# list are mutable
# list uses indexing and slicing
x=["abc",1, 2.5e-1, 5+1j]
print(x)

# another way to create list

x=list('abc')
print(x)
x=list((1,2,3))
print(x)

# access list element by index
# index starts with 0

print(x[1])

# python allows negative indexing starts with -1
# -1 index points to the last element of the list
print(x[-1])

# nested list
y=[1,[1,2, [3,4]], (1,2,3),{1,2}]
print(y)

# Access nested list items
print(y[1][2][1])
print(y[3])


# slicing
# it is used to extract subpart of a iterable

l=['a','b','c','d','e']
print(l[1:3])
print(l[:-1]) # by default slicing starts with 0
print(l[-4:-2])

# it also includes a third parameter jump
print(l[::2]) # prints elements at even indices

print(l[::-1]) # it will reverse the list
print('*******')
print(l[::-2])

# we can also change item value
l[1]="B"
print(l)

# add items to a list
l.append('f')
print(l)

l.insert(2,"C")
print(l)

# remove items from list
# remove value by index
l.pop(1) # by default if you dont give the index it will pop out last element
print(l)

# remove by value
l.remove("f")


# to add two list
# extend method
l.extend(x)
print(l)

