# Every dictionary has two parts 1. Key 2. Value
# On the left hand side is key and right hand side is value
# {"Key":"Value"}

users_dict = {
    "Id": 100,
    "FullName": "Chakrapani U",
    "EmailId": "Chakrapan@Test.com",
    "Phone": "9099999999",
    "Status": "Active",
}

print(users_dict)

# adding item to dict
users_dict["DateCreated"]="10-10-2021"
print(users_dict)

# getting specific data
print(users_dict["EmailId"])

# getting specific data, Dict will throw the error if searching key not present in dict
# print(users_dict["EmailId1"])
# Traceback (most recent call last):
#   File "e:\Python Programming\Python\12_dictionary.py", line 23, in <module>
#     print(users_dict[0])
# KeyError: 0

# updating the data
users_dict["EmailId"] = "chakra24@test.com"
print(users_dict)

# The pop() method removes the item with the specified key name
users_dict.pop("DateCreated")
print(users_dict)

# The popitem() method removes the last inserted item
users_dict.popitem()
print(users_dict)
