   
sandvitchs = [' onesen', ' pastrami' , ' twosen', ' pastrami' , ' threesen' , ' pastrami']
dones = []
out_sendwitchs = []

print("We are out of pastrami")

while sandvitchs:
    for sands in sandvitchs:
        if sands == ' pastrami':
            sandvitchs.remove(' pastrami')
    orders = sandvitchs.pop()
    print("procesing" + orders)
    dones.append(orders)
    
print('Dones sandwichs')
for done in dones:
    print(done.title())