#Katrina Ventura
#November 6, 2023
#Homework 2

#First, ask how old the user is.
#In that time, how many times the user's heart has beaten.
#In that time, how many times a blue whale's heart has beaten.
#In that time, how many times a rabbit's heart has beaten. If the answer to rabbit heartbeats is more than a billion, say "XXX billion" instead of the very long raw number
#There are several ways to calculate and format/display numbers in Python – string addition, f-strings, commas, etc etc etc. Redo one of the above questions above with another technique and briefly explain the pros and cons of each approach.


age = input("Please enter age")
age = int(age)
print("In that time, your heart has beaten", age * 80 * 60 * 24 * 365, "times")
print(f'In that time, a blue whale heart has beaten {age * 33 * 60 * 24 * 365} times')
print("In that time, a rabbit heart has beaten", age * 120 * 60 * 24 * 365/1000000000, "billion times")
if age > 27:
    print("You are", age - 27, "year/s older than me.")
if age == 27:
    print("We're the same age")
if age < 27:
    print("You are", 27 - age, "year/s younger than me")


#Next, ask which year the user was born.
#If they were born in an even or odd year
#How many times there has been a president from the Democratic Party in office since they were born (1980 onward, and each president only counts once)


year = input("Now, please enter your year of birth")
year = int(year)
if (year % 2) == 0:
    print("You were born in an even year")
else:
    print("You were born in an odd year")

#How many times there has been a president from the Democratic Party in office since they were born (1980 onward, and each president only counts once)

#4 democratic presidents since 1980
#jimmy carter 1977 to 1981
#bill clinton 1993 to 2001
#obama 2009 to 2017
#joe biden 2021 to 2024

year = input("Now, please enter your year of birth")
year = int(year) 
if year < 1980:
    print("4 US Presidents from the Democratic Party have been elected")
if year < 2001:
    print("3 US Presidents from the Democratic Party have been elected")
if year < 2017:
    print("2 US Presidents from the Democratic Party have been elected")
else:
    print("1 US President from the Democratic Party have been elected")


#Which US President was in office when they were born (1980 onward)

year = input("Now, please enter your year of birth")
year = int(year) 
if year < 1982:
    print("The President was Jimmy Carter")
if year < 1989:
    print("The President was Ronald Reagan")
if year < 1993:
    print("The President was George Bush")
if year < 2001:
    print("The President was Bill Clinton")
if year < 2009:
    print("The President was George W Bush")
if year < 2017:
    print("The President was Barack Obama")
if year < 2021:
    print("The President was Donald Trump")
if year < 2023:
    print("The President is Joe Biden")


#Can you think of another approach to #7 and/or #8 that you could have tried? Why is yours better? If you could not get #7/#8 to work, use this question to explain what you were trying to do.
## I could use a loop maybe? 

#If someone says they were born in the future, ask them for their year of birth again. Assume they'll do it right the second time.

year = input("Now, please enter your year of birth")
year = int(year) 
if year > 2023:
  print("Please enter your birth year again")
  year = input("Please enter your year of birth again")
else:
  print("Thank you")

