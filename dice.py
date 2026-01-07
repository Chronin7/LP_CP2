#import a random module
#define roll dice with peramaters of dice size count and if advantage is true none or false
# make doc string
# if advantage is true take the max of 2 random numbers and return it
# if none than roll count of dice dice and put them in a list and return it
# if False than take min of 2 random numbers and return it
from utill_functions import alternate_random
def roll_dice(dice_size,dice_count,advantage=None):
    """advantage is none for normal (this is the only time that it will roll that many dice)
        True for advantage
        False for disadvantage
    """
    if advantage == True:
        return max(alternate_random((1,dice_size),int),alternate_random((1,dice_size),int))
    elif advantage == None:
        rolls=[]
        for x in range(1,dice_count):
            rolls.append(alternate_random((1,dice_size),int))
        return rolls
    elif advantage == False:
        return min(alternate_random((1,dice_size),int),alternate_random((1,dice_size),int))

