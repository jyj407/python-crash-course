filename = 'guest.txt'

with open(filename, 'a') as file_object:
    full_name = input("Please provide your full name: ")
    file_object.write(full_name + "\n")
