#wap to convert the days into years ,weeks,and days'

#Take input
days = int(input('Enter the days:'))

# perform operation
years = days // 365
remaining_days =  days % 365
weeks = remaining_days // 7
final_day = remaining_days % 7



# display result
print(f' The convertion of {days} days into years is {years} years ,weeks is {weeks} weeks, finaldays is {final_day} days')