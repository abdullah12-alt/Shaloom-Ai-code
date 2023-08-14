
# num_1=int(input("enter any number: "))
# sum_1=0
# for a in range(1,num_1):
#     sum_1=sum_1+a
    
# print(sum_1)


# fabnaici series

# num1=0
# num2=1

# num1,num2=0,1


# for a in range(10):
#     print(num1, end="  ")
#     prev= num1+num2 
#     num1=num2
#     num2=prev


# factorial
def fac(num):
    factorial =1
    if num<0:
        print('fac is not possible of this num')
    elif num==0:
        print('fac of O is 1')
    else:
        for i in range(1,num+1):
            factorial=factorial*i
        print(factorial)
    
num=int(input('enter the num : '))    
fac(num)
             
        
        
        
