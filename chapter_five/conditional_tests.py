age = 18
friend_age = 19

if friend_age >= age:
    print("you are not friends")

name = "Amir"

if name.lower() == "amir":
    print("Your name is Amir")
    
number = 1

if number == 9 :
    print("Your number is 9")
    
if number != 9 :
    print("Your number is not 9")
    
if number < 9 :
    print("Your number is less than 9") 
    
if number > 9 :
    print("Your number is greater than 9")
    
value1 = 9
value2 = 8

if value1 == 9 and value2 != 9 :
    print("Your number is 9")
else:
    print("evvv")
    
numbers = [value for value in range(1, 10)]

if 9 in  numbers:
    print("number 9 in your list")
else:
    print("number 9 not in your list")
    
    
banned_users = ['andrew', 'carolina', 'david']

user = 'marie'

if user not in banned_users:
    print("your welcome")
else:
    print("go out")
    
    
age = 19

if age <= 4:
    price = 0
elif age < 18 :
    price = 5
else:
    price = 10
print(price)