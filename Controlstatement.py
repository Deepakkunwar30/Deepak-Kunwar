# x = 5
# y = 7
# if x>y:
#     print('x is greater')
# elif x==y:
#     print('x is equal to y')
# else:
#     print('y is greater than x')

# a = 5
# b = 5 
# c = 60
# if a>b and b>c:
#     print('a is greater')
# elif b>a and b>c:
#     print('b is greater')
# else:
#     print('c is greater')
# Q1 
# WAP to enter any number and check wheather it is even or odd?
# number1 = int (input('Enter any number'))
# if number1/2:
#     print('The inputed number is even')
# else:
#     print('The entered number is odd')

# Q2
# WAP to enter any number and check wheather it is divisiable by 3 and 5?
# number2 = int (input('Enter any number'))
# if number2/2 and number2/5:
#     print('The inputed number is divisiable by 3 and 5 even')
# else:
#     print('The entered number is not divisiable by 3 and 5')

# Q3
# WAP to enter age and check wheather the person eligible for vote or not?
# age = int (input('Enter your age'))
# if age>18 and age<48:
#     print('The person is eligable to cast vote')
# else:
#     print('The person is not eligable to cast vote')

# Q4
# WAP to enter five subject marks and calculate the total percentage and grade?
# math = 80
# english = 60
# nepali = 30
# social = 32
# physics = 45
# math = float(input('Enter mark\'s of math'))
# english = float(input('Enter mark\'s of english'))
# nepali = float(input('Enter mark\'s of nepali'))
# social = float(input('Enter mark\'s of social'))
# physics = float(input('Enter mark\'s of physics'))

# Total_average_marks = (math+english+nepali+social+physics)/5
# Percentage = (Total_average_marks/500)*100
# print('The total per: '+str(Percentage))

# if Total_average_marks>35 and Total_average_marks<45:
#     print('Grade C')
# elif Total_average_marks>45 and Total_average_marks<60:
#     print('Grade B')
# elif Total_average_marks>60 and Total_average_marks<75:
#     print('Grade A')
# elif Total_average_marks>75 and Total_average_marks<100:
#     print('Grade A+')
# else: 
#      print('Fail')
# Q5
# WAP for mini calculator
# choice = int (input('Enter your choice'))
# if choice == 1:
#     a = int (input ('Enter first number'))
#     b = int (input ('Enter second number'))
#     sum = a + b
#     print('sum:'+ str(sum))

# elif choice == 2 :
#     a = int (input ('Enter first number'))
#     b = int (input ('Enter second number'))
#     sub = a - b
#     print('subtraction:'+ str(sub))

# elif choice == 3:
#     a = int (input ('Enter first number'))
#     b = int (input ('Enter second number'))
#     mul = a * b
#     print('multiplication:'+ str(mul))
# elif choice == 4:
#     a = int (input ('Enter first number'))
#     b = int (input ('Enter second number'))
#     div = a % b
#     print('Division:'+ str(div))

# Q6

username = input('Enter your user name')
password = input('Enter you password')

if username == 'admin':
    if password  == 'admin':
        print('Welcome admin')
    else:
        print('Invalid password')

else:
    print('Invalid username')

