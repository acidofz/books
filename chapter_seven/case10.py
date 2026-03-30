locations = []
user = ''
active = True

while active == True:
    user = input("your location ")
    locations.append(user)
    if user == 'quit':
        active = False
        locations.remove('quit')
print(locations)