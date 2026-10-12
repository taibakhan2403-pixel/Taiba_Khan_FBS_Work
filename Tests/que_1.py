#Write a program to find the area and perimeter of
#following figure (Accept the length, breadth and radius from user:

l = int(input('Enter length: '))
b = int(input('Enter breadth: '))
r = int(input('Enter radius:'))

area = (l*b) + (3.14*r*r/2)
perimeter = l+(2*b) + (3.14* r)


print("Area of figure =",area)
print("Perimeter of figure =",perimeter)

