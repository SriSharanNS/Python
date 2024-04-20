import random
class Dice:
        def Diceroll(self):
            first=random.randrange(1,6)
            second=random.randrange(1,6)
            return first,second

dice=Dice()
print(dice.Diceroll())