users = ['admin', 'tony', 'jessica', 'james', 'xiaoyangyang']
#users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + ", would you like to see a status report?")
        else:
            print("Thank you for logging in again " + user)
    
else:
    print("We need to find some users!")
