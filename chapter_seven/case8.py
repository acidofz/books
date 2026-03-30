unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
    # sandvitchs
    
sandvitchs = [' onesen', ' twosen', ' threesen']
dones = []

while sandvitchs:
    orders = sandvitchs.pop()
    print("procesing" + orders)
    dones.append(orders)
    
print('Dones sandwichs')
for done in dones:
    print(done.title())