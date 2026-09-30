#calculate sellling price of book based on cost price and discount
#Take input
CP = int(input('Enter the CP:'))
Dis = int(input('Enter the Dis:'))

#perform operation
Dis = CP * Dis / 100
SP = CP - Dis

#display
print(f'The selling price is {SP}')


