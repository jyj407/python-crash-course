sa = input("Intput the first number: ")
sb = input("Intput the first number: ")
try:
    a = int(sa)
    b = int(sb) 
    sum = a + b
except ValueError:
    msg = "Sorry, you input an invalid number!"
    print(msg)
else:
    print("sum of " + str(a) + " + " + str(b) + " = " + str(sum))

