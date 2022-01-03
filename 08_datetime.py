# importing datetime library
import datetime

# get todays date
print(datetime.date.today())

# get current year
print(datetime.date.today().year)

# get current month
print(datetime.date.today().month)

# get current day
print(datetime.date.today().day)

# ctime(const time_t *timer) returns a string representing the localtime based on the argument timer.
print(datetime.date.today().ctime())