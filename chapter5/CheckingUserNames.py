current_users = ['admin', 'tony', 'jessica', 'james', 'xiaoyangyang']
new_users = ['admin', 'Mark', 'Jessica', 'james', 'xiaoyangyang']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Hello " + new_user + ", you need to come up a new user name")
    else:
        print("The user name: " + new_user + " is available")
        current_users.append(new_user.lower())

print(current_users)
