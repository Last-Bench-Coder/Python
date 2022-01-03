#In previous example we have done string concatination by using + operator
#It works fine, but what if we have more items to concatinate
#Also conversion will be hectic part when we do concatination(We cannot concatinate one datatype with other)
#f-strings will helps lot avoid type conversion and also code looks cleaner
#f-strings released in python 3, we need to use "f" and variable will be mentioned within "{}"
# Here is sample print(f"Your string {variable}")

name = input("Enter your name : ")
age = int(input("Enter your age  : "))

# String concatination using + Operator
print("Hello "+name+" Welcome your age is "+str(age))

# Above we have used + operator to concatinate, we need to maintain 
# space between values and also type conversion
# f-strings want require like this
print(f"Hello {name} Welcome your age is {age}")

