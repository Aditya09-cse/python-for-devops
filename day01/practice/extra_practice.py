# 1. Write a program to check if a number is positive, negative, or zero ?
'''
num = int(input("Enter the number : " ))
if num > 0:
    print(f"The number is positive {num}")
elif num <0 :
    print(f"The number is negative {num}")
elif num == 0 :
    print(f"The number is zero : {num}")
else :
    print("Number is not positive , negative and zero") '''

# 2. Take a year as input and check if it is a leap year ?
'''
check_year = int(input("Enter the year : " ))
if check_year % 400 :
    print("year is leap year")
elif check_year % 100 :
    print("not a leap year")
elif check_year % 4 :
    print("year is leap year")
else :
    print("not a leap year")
    '''

# 3. Accept three numbers and print the largest ?
'''
num1 = int(input("Enter num1 : " ))
num2 = int(input("Enter num2 : " ))
num3 = int(input("Enter num3 : " ))
if num1 > num2 and num1 > num3 :
    print ("num1 is largest")
elif num2 > num3 :
    print("num2 is largest")
elif num3 > num2 :
  print("num3 is largest")
else :
    print("numbers are equal")
    '''

# 4. Check if a given character is a vowel or consonant?
'''
alphabet = (input("enter the alphabet : " )) 
if alphabet in 'aeiouAEIOU' : # for check membership  use 'in' instead of '=='
    print("given char is vowel")
else :
    print("given char is consonant ")
    '''

# 5. Accept a number and check if it is even or odd ?
'''
num = int(input("Enter the number :" ))
if num % 2 == 0 :
    print("Given number is even")
elif num % 2 != 0 :
    print("NUmber is odd ")
else :
    print("number is not even & odd ")
    '''
####################################################

# 2. Loops

# Print numbers from 1 to 100 using a for loop
'''
for i in range(1,101) :
    print(i)
'''

# Print the multiplication table of a given number
'''
num = int(input("Enter the number for table to print :" ))
for i in range(1,11) :
    print(f"{num} * {i} = {num*i}")
'''

# Calculate the sum of digits of a number.
'''
num = int(input("enter the number :" ))
sum_of_digits = 0
while num > 0 :
    digit = num % 10 # it will give you the last digit of number
    sum_of_digits += digit # add last digit into sum of digit
    num //= 10 # remove last digit
print("the sum of digits are :" ,sum_of_digits)
'''

# Reverse a given integer without converting it to a string
'''
num = int(input("enter the number for reverse the order :" ))
rev = 0
while num > 0 :
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(rev)

'''

# Print all prime numbers between 1 and 100



