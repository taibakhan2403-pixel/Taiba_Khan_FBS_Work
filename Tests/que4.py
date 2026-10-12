#Calculate the cost of painting the following building’s walls (both interior and
#exterior). You need to accept area (one wall) and cost of both interior and
#exterior wall.
#(Note: 1. Below diagram is of two joint rooms.
#2. It is upper view of building.)

area = int(input('Enter area of one wall: '))
interior = int(input('Enter cost of interior: '))
exterior = int(input('Enter cost of exterior: '))

total_walls = 7
i_c = area * total_walls * interior
e_c = area * total_walls * exterior

total_costs = i_c + e_c
print(f'The interior painting cost {i_c}')
print(f'The exterior painting cost {e_c}')