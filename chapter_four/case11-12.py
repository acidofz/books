pizzas = ['pepperoni', 'margherita', 'hawaiian']
pizzas.append('superchess')

friend_pizzas = pizzas[:]
friend_pizzas.append('supersoup')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
    
print("My friend favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)