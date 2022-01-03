#string to int conversion
#when we read any input from cmd it will be string
#we get converion error str to int/float/bool conversion error
#we need to convert the same to required datatype

print("Welcome to Age Calculator")
yob = input("Enter your year of birth : ")

#Converting string to int
age = 2022 - int(yob)

#Converting int to str is not possible
print("Your age is : "+str(age))