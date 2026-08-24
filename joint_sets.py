# set methods
# union() - join iterables and returns a new one
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set4 = {"x", "y", "z"}
tup1 = (10, 11, 12)
list1 = [90, 91, 92]

set3 = set1.union(set2, set4, tup1, list1)
print(set3)

print(set1)

# set methods
# update() - join iterales and modifies the original one
set99 = {"a", "b", "c"}
set100 = {1, 2, 3}
set400 = {"x", "y", "z"}
tup10 = (10, 11, 12)
list111 = [90, 91, 92]

set99.update(set99, set100, tup10, list111)
print(set99)

# intersection() - returns a new set and only contains items that are present/common in both sets
# intersection_update()
set123 = {"apple", "banana", "cherry"}
set213 = {"google", "microsoft", "apple"}
set313 = set123.intersection_update(set213)
print(set313)

# difference()- return a new set that will contain only the items from the first set that are not present in the other set.
# difference_update()
set1ac = {"apple", "banana", "cherry"}
set2wv = {"google", "microsoft", "apple"}

set3rt = set1ac.difference(set2wv)
print(set3rt)

# symmetric_difference
# symmetric_difference_update()
set1ui = {"apple", "banana", "cherry"}
set2df = {"google", "microsoft", "apple"}

set3rtrt = set1ui.symmetric_difference(set2df)
print(set3rtrt)

# frozenset
# no add or remove option

x = frozenset({"apple", "banan", "cherry"})
print(x)
print(type(x))