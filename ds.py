thistuple = ("apple", "banana", "cherry")
print(thistuple)


# thistuple[0]='mango'

# print(thistuple)


fruits = ("apple", "banana", "cherry","mango","pineapple")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ["apple", "banana","apple", "cherry","mango","apple","pineapple"]

print(fruits)
fruits=set(fruits)

fruits=list(fruits)
print(fruits)



thisdict = {
  "brands": {'brand1':"civic","brand2":"bmw"},
  "model": "Mustang",
  "year": 1964
}



# print(thisdict)
print(thisdict["brands"]['brand1'])
# print(thisdict['model'])



# print(thisdict.keys())
# print(thisdict.values())



