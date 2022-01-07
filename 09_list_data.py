# list are used to hold the different types of data in one variable
# list can hold the duplicate data
# list is mutable, we can add/update/delete the data in it

# below list contain different types of data string, integer, float
data = ["Chakrapani", 100, 10.5]
print(data)

# Insert New Data using insert method
# insert method helps us to insert the records in specific location
# below we are inserting the data after index 2
data.insert(2,"Shraddha")
print(data)

# Insert New Data using append method
# append method helps us to insert the records at last
data.append("Shreshta")
print(data)

# Insert duplicate data
data.append("Shreshta")
print(data)

# update
data[2]="Test"
print(data)

# delete the data with remove key word
# it will revove the data based on value
# it does not return any deleted data
data.remove("Test")
print(data)

# delete the data with pop() method
# it will revove the data based on index
# it will return deleted data
rec = data.pop(2)
print(rec)
print(data)