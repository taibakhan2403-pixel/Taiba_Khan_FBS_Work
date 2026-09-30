#wap to swap two numbers using third varibale

##Take input
x = int(input('Enter the num1: '))
y = int(input('Enter the num2: '))

#Perform operation
x = x + y
y = x - y
x = x - y

#Display result
print(f'The swapped numbers are {x} and {y}')