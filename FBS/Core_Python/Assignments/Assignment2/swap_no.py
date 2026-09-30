#wap to swap two numbers using third varibale
##Take input
x = int(input('Enter the num1: '))
y = int(input('Enter the num2: '))

#Perform operation
z = y
y = x
x = z

#display result
print(f'The swapped numbers are {x} and {y}')