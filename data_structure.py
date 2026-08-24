# python data structures
# list - indexed, ordered, duplicates, mutable
# create list
fruits = ["apple", "guava", "grapes", "mango", "grapes", "grapes"]
veggies = list(("potato", "tomato", "chilli", "potato"))

# checking whether list or not
print(type(fruits))
print(type(veggies))

# access list items
print(fruits[0])
print(veggies[0])
print(fruits[3])

# length of the list
# len(list)
print(len(fruits))
print(len(veggies))

# insert items into the list at the end
# append(item)
fruits.append("strawberry")
fruits.append("kiwi")
print(fruits)
print(len(fruits))

# sorting the list - ascending order 
# sort()
fruits.sort()
print(fruits)

# sorting the list  - descending order
# sort(revese = True)
fruits.sort(reverse = True)
print(fruits)

# slicing a list - cutting a list
# [start index: end index+1]

cities = ["New Delhi", "New York", "New Jersey", "Dublin", "Texas", "California", "Chicago", "Port Blair", "Jakarta"]
print(cities[2:8])
print(cities)

# concatenation of lists
# extend(list)
fruits.extend(veggies)
fruits.extend(cities)
print(fruits)

# removing the last item form the list
# pop()
fruits.pop()
print(fruits)

# remove an item using the index number
# pop(index)
fruits.pop(1)
print(fruits)

# remove an item by its name
# remove(item name)
fruits.remove("apple")
print(fruits)

# count how many times an item is repeated inside the list
# count(item)
print(fruits.count("grapes"))
print(fruits.count("potato"))

# copy - copying the list
# copy()
myList = fruits.copy()
print(myList)

# mix list
myMixedList = ['tom', 12, 5.6, True]
print(myMixedList)
print(myMixedList[2])

# insert - inserting an item into the list at a given index number
# insert(index, item)
fruits.insert(0, 'pineapple')
print(fruits)

# finding the index number of a particular item
# index(item)
print(fruits.index('grapes'))

# clear a list
# clear()
fruits.clear()
print(fruits)

# delete a list
# del list
del fruits
# print(fruits)


# dictionary - "key":value - ordered, unique, unindexed, mutable
person = {
    "name": "Rohit",
    "age": 24,
    "marks": 75.5,
    "isStudent": True,
    "fav_food": ["Chicken Biriyani", "Panner Butter Masala", "Cakes", "Ice-cream"]
}

# access the dictionary
print(person)
print(type(person))
print(person["name"])
print(person["age"])

# updating a dictionary
person["fav_color"] = "black"
print(person)

# length of the dict
print(len(person))

# remove from the dict
# pop("key")
person.pop("marks")
print(person)

# popitem()- removes the last dic item
person.popitem()
print(person)

# clear() - clear all items
person.clear()
print(person)

# delete a dictionary
# del dict
del person
# print(person)