# Wap to calculate total salary of employee based on basic ,da=10% of basic,ta=12% of basic,hra=15% of basic

#take input
basic_salary = int(input('Enter the salary:'))

#perform operation
da = basic_salary * 10 / 100
ta = basic_salary * 12 / 100
hra = basic_salary * 15 / 100
total_salary = basic_salary + da + ta + hra

#Display
print(f'The total saalry is {total_salary}')