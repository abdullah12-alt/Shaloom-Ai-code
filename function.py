

def table(value):
    print(f'we are print the table of : {value}')
    a=1
    while a<=10:
        print(f"{value} x "+str(a) + " = "+str(value*a))
        a=a+1  


table(2)
table(3)
table(4)

# print(type(a))

def Info(name,*kids):  #parameter
   print(f'{name} is father of {kids[0]} \t ,{kids[1]},\t {kids[2]}')
    
Info('Arif','asim','ali','atif') #argumant



def seasonalFruites(season,fruits):
     pass
#     print(f"These the {season} fruites\n{ fruits }")

seasonalFruites('summer',['mango','banana','peach'])

