#wap to reverse 3 digit no.

#Take input
num = int(input('Enter the 3 digit  no.:'))
rev = 0

#perform operation

while num > 0:
 t = num % 10          # last digit
 rev = rev * 10 + t    # add in reverse
 num = num // 10       # last digit remove

#display 
print(f'The reverse of 3 digit no. is {rev}')