
age = 12
if age < 4:
        price = 0
elif age < 18:
        price = 5
else:
        price = 10
print("Your admission cost is " + str(price) + ".")


requested_toppings = ['mushroom', 'extra cheese']
if 'mushroom' in requested_toppings:
        print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
        print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
        print("Adding extra cheese.")
print("\nFinished making your pizza!")
