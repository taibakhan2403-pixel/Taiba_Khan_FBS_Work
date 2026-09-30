#  value check nhi krta memory addresss check krta
# mutable 
#single value is always immutable resuse nhi kr skhte
#can change into original object(addess) 
#cant resuse
#list memeory address different

#immutable

#reuse kr skhte hai 
#cant change into original object(address)
#can resuse
#int memory address same

x = 10
y = 10
li1 = [10,20]
li2 = [10,20]

#1. is 
print(x is y)
print (id(x))
print(id(y))
print(li1 is li2)
print(id(li1))
print(id(li2))

#2. is not
print(x is not y)