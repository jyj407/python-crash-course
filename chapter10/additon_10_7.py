while (True):
    sa = input("Intput the first number: ")
    if (sa == 'q'):
        break
    sb = input("Intput the first number: ")
    if (sb == 'q'):
        break

    try:
        a = int(sa)
        b = int(sb) 
        sum = a + b
    except ValueError:
        msg = "Sorry, you input an invalid number!"
        print(msg)
    else:
        print("sum of " + str(a) + " + " + str(b) + " = " + str(sum))
    
