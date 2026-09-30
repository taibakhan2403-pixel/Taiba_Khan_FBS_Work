#convert feet and inch into meter and centimeter

#Take input
feet = int(input('Enter the feet:'))
inch = int(input('Enter the inch:'))

#Perform operation
meter = 0.3048 * feet
centimeter = 2.54 * inch

#Dsiplay
print(f'The conersion of feet into {meter} meter & inch into {centimeter} centimeter')
