x=[1,2,3]
y=[1,2,3]

# Returns true if x and y are same object
print(x is y)

x=2
y=2
print(x is y)

x="Giraj"
y="Giraj"
print(x is y)

# Returns True if x and y are different objects 
x=(1,2,3)
y=(1,2,3)
print(x is not y) 

x=[1,2,3]
y=[1,2,3]
print(x is not y)