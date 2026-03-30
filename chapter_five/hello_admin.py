# users = ['amir', 'daler', 'ifti', 'farzod', 'admin']
# for user in users:
    # if user == 'admin':
        # print("Hello admin, would you like to see a status report?")
    # else:
#          print("Hello " + user)
        
# users = []
# if users:
#     for user in users:
#         print("Hello " + user)
# else:
#         print("We need to find some users!")

current_users = ['amir', 'daler', 'ifti', 'farzod','amin', 'john']
new_users = ['amir', 'farxunda', 'sabrina','amalya','daler', 'JOHN']

if  new_users:
    for new_user in new_users:
        if new_user.lower() in current_users:
            print("Please enter a new username")
        else:
            print("Username is available")
