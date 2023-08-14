# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

x=3

print(not(x >5 or  x < 10))


mylist = ["apple", "banana", "cherry", True,2.0,3]
print(type(mylist))
print(mylist[0])
print(len(mylist))


mylist[2]='mango'
print(mylist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "watermelon")
print(thislist)



thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)