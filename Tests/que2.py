#Write a program to calculate simple interest based on Principal, Rate and Time
#(SI = P*R*T/100)


a = int(input('Enter the value of p:'))
b = int(input('Enter the value of t:'))
c = int(input('Enter the value of r:'))

Si = (a*b*c)/100
print(f'{Si} is the simple interest ')