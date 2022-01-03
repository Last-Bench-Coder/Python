#As like f-strings we have another way to do it 
#that is .format(function), we keep empty place holder, 
#later we will assign the value with the help of format method

name = input("Enter your name : ")
age = int(input("Enter your age  : "))

# String concatination using + Operator
print("Hello "+name+" Welcome your age is "+str(age))

# Above we have used + operator to concatinate, we need to maintain 
# space between values and also type conversion
# format want require like this
print("Hello {} Welcome your age is {}".format(name,age))

#Also we can do like this
message = "Hello {} Welcome your age is {}"
final_output = message.format(name,age)
print(final_output)

# In aboue example we need to mention the value in order name 
# first and age later inside format method, if we change the order then our output 
# will be different, name place age will get displayed and age place name, 
message = "Hello {} Welcome your age is {}"
final_output = message.format(age,name)
print(final_output)

# To avoid this we can use keys shown below
message = "Hello {n} Welcome your age is {a}"
final_output = message.format(a=age,n=name)
print(final_output)