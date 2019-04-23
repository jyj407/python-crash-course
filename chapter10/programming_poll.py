filename = 'poll.txt'
with open(filename, 'a') as file_object:
    while (True):
        reason = input("Why do you like progamming? ")
        if (reason == "q"):
            break
        else:
            file_object.write("I likes progamming because " + reason + "\n")
    
    
