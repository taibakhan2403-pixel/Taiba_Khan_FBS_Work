#Covert the time of hh,min and sec into sec
#Take input
hh =  int(input('Enter hours:'))
min = int(input('Enter minutes:'))
sec = int(input('Enter seconds:'))
#perform operation
hours_in_sec = 60*60*sec
min_in_sec = 60*sec
total_sec = hours_in_sec + min_in_sec
#display
print(f'The time entered is {total_sec}')