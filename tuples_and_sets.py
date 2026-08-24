# tuple - ordered, indexed, immutable, allow duplicates

# creation
fruits = ("apple", "orange", "kiwi")
print(fruits)
print(type(fruits))

# another way for tuple creation
veggies = tuple(("potato", "chilli", "onion"))
print(type(veggies))

# find the number of elements
print(len(fruits))

# access the tuple element 
print(fruits[0])
print(veggies[1])
print(fruits[-1])

# slicing a tuple
colors = ("red", "blue", "green", "orange", "purple", "violet", "indigo", "yellow")
print(colors[2:5])

# check if an item exists
print("indigo" in colors)
print("pink" in colors)

# updating a tuple
fruitsList = list(fruits)
fruitsList.append("papaya")
fruitsList.insert(1, "grapes")
fruitsList.remove("kiwi")
fruits = tuple(fruitsList)
print(fruits)

# upacking a tuple
friends = ("Garry", "Peter", "Kevin")
(friend1, friend2, friend3) = friends
print(friend1)

cars = ("Audi", "BMW", "Ferrari", "Porche", "Ford", "Hyndai", "Audi")
(car1, car2, *morecars) = cars
print(car1)
print(car2)
print(morecars)
print(type(morecars))

# looping over tuples
for fruit in fruits:
  print(fruit)

i = 0
while(i < len(fruits)):
  print(fruits[i])
  i += 1

for i in range(len(fruits)):
  print(fruits[i])

# joining tuples - create a new tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# count()
print(cars.count("Audi"))

# index()
print(cars.index("Porche"))

# sets -unordered, unindexed, unique, immutable
fruits1 = {"apple", "orange", "kiwi", "apple"}
print(fruits1)
print(type(fruits1))

fruits2 = set(("apple", "orange", "kiwi"))
print(fruits2)
print(type(fruits2))

# length of the set
print(len(fruits1))

# access/change - can not access set item via index number as sets are unindexed

# where an item exists in set or not
print("kiwi" in fruits1)
print("papaya" not in fruits1)

# add items to set
fruits1.add("watermelon")
print(fruits1)

# remove item from set
fruits1.remove("watermelon")
print(fruits1)

# update() - adding or joining sets/list/tuple together
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
list1 = [4, 5, 6]
tuple1 = (7, 8, 9)

set1.update(set2, list1, tuple1)
print(set1)

# use loop that does not involve index numbers
for fruit in fruits1:
  print(fruit)