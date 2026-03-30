pizza = []
it = ''
while it != 'quit':
    it = input("What pizza do you like? ")
    if it != 'quit':
        pizza.append(it)
print(pizza)