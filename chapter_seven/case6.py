pizza = []
it = ''
active = True
while active == True:
    it = input("What pizza do you like? ")
    pizza.append(it)
    if it == 'quit':
        active = False
print(pizza)