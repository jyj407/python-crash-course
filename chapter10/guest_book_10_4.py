filename = 'guest_book.txt'
with open(filename, 'a') as file_object:
    while (True):
        fullname = input("Input your full name please: ")
        if (fullname == "q"):
            break
        else:
            print("Hello " + fullname)
            file_object.write(fullname + " visited us.\n")
    
    
