
# User will input (3ages).Find the oldest one

# age1= int(input('enter age 1 : '))
# age2= int(input('enter age 2 : '))
# age3= int(input('enter age 3 : '))

# if age1>age2 and age1>age3:
#     print(f'age one is greater than all : {age1}')
# elif age2>age1 and age2>age3:
#     print(f'age two is greater than all : {age2}')
# else:
#     print(f'age three is greater than all : {age3}')
    
    # Write a program that will convert celsius value to fahrenheit
   
# (Temperature in degrees Celsius (°C) * 9/5) + 32
    
# Cel= int(input('Enter the temp in celsius'))

# convert=(Cel*9/5)+32

# print(f"Temp in fahrenheit : {convert}")


# User will input (2numbers).Write a program to swap the numbers
# a= int(input('Enter the value for a :'))
# b= int(input('Enter the value for b :'))
# print(f"The value of a is {a} and b is {b} before swap")

# temp=a
# a=b
# b=temp
# print(f"The value of a is {a} and b is {b} after swap")


# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
# num = 1234
# reversed_num=0

# while num!=0:
#     digit= num %10 #4  3  2  1
#     reversed_num=reversed_num*10+digit #4  43 432  4321
#     num =num//10   #123 12  1  0
    
# print(reversed_num)
    
# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.


angle1= int(input('Enter first angle :'))
angle2= int(input('Enter sec angle :'))
angle3= int(input('Enter third angle :'))

Sum=angle1+angle2+angle3
if(Sum==180):
    print("Its a triangle")
else:
    print("Not a triangle")