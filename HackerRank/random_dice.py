import random


class Dice:
    def Roll(self):
        first_number = random.randint(1, 6)
        second_number = random.randint(1, 6)
        return first_number, second_number


dice1 = Dice()
roll_sides = dice1.Roll()
print(roll_sides)
