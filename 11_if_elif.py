# Based on condition we can execute some statements
# if elif help us to do

print("Welcome To Leap Year Check")
year = int(input("Enter year you need to check : "))

if (year % 100==0 and year % 400==0) or (year%100!=0 and year % 4 ==0):
    print("Leap Year")
else:
    print("Not Leap Year")
