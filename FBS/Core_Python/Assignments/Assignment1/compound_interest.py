# WAP to clculate the compound interest
#Take input
p = int(input('Enter the value of Principal:'))
t = int(input('Enter the value of Time:'))
r = int(input('Enter the value of Rate:'))
#Perform operation
a = p * (1+r/100) ** t
ci = a - p
#display
print(f'The compund Interest is {ci}')