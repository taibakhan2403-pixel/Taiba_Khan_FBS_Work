#wap to find roots of quadratic equation

a = int(input('Enter the value of a:')) # 1
b = int(input('Enter the value of b:'))  #-5
c = int(input('Enter the value of c:'))  #6

#perform operation
D = b**2 - 4*a*c
x1 = (-b + D ** 0.5) / (2*a)
x2 = (-b - D ** 0.5) / (2*a)

#display result
print(f'The value of rooots of Q.E is{x1} & {x2}')