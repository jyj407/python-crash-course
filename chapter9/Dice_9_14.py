from random import randint

class Dice():
    def __init__(self, side = 6):
        self.side = side

    def roll_dice(self):
        side = randint(1, 6)
        self.side = side

    def show_side(self):
        print("The current side is " + str(self.side))


dice6 = Dice()
dice6.show_side()

print("Now rolling the dice 10 times")
count = 0 
for i in range(1, 11):
    dice6.roll_dice()
    dice6.show_side()

print(count)
