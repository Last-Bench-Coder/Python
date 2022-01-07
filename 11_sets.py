# sets are used to hold the different types of data in one variable
# sets do not allow duplicate values
# sets is mutable, we can add/remove the data in it
# sets will be declared with {} symbol
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

s = {"Chakrapani","Shraddha",100,10.5}
print(s)

# adding the data
s.add("Shreshta")
print(s)

# add duplicate data
# it will not have duplicate data
s.add("Shreshta")
print(s)

# delete the data with remove key word
# it will revove the data based on value
# it does not return any deleted data
s.remove("Shreshta")
print(s)

# removing the data with pop, pop deletes last items
# it will return deleted data
deleted = s.pop()
print(deleted)
print(s)