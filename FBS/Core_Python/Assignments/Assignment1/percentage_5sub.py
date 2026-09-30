#write a prg to calaculate the percentage of student based on marks of any subject

#Take input
sub1 = int(input('Enter the first subject marks:'))
sub2 = int(input('Enter the second subject marks:'))
sub3 = int(input('Enter the third subject marks:'))
sub4 = int(input('Enter the fourth subject marks:'))
sub5 = int(input('Enter the fifth subject marks:'))
#perform  calculation
marks = sub1+sub2+sub3+sub4+sub5
#perform operation
percentage = (marks/500) * 100
#Dsiplay 
print(f'The percentage of student is {percentage}')
