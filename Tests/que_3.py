#Write a program to accept distance in km and convert it into meters and
#centimeters both.

km = int(input('Enter the value: '))
m = km*1000
cm = km*100000

print(f'The distance in meters is {m}')
print(f'The distance in centimeters is {cm}')