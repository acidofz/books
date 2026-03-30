price1 = 0
price2 = 10
price3 = 15

while age > 0:
    if age <= 3:
        print(f"Your ticket price is {price1}")
    elif age <= 12:
        print(f"Your ticket price is {price2}")
    else:
        print(f"Your ticket price is {price3}")
    age = int(input("Your age"))