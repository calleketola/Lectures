import random

def roll_dice(n, exploding = True, sides = 6):
    """
    n:int number of dice to roll
    exploding:bool reroll rolls of highest side
    sides:int number of sides on the die

    A function that rolls n dice and lets "sixes"
    explode, i.e. you remove any rolled six and
    roll two new dice. This pushes the expected
    value of a die roll from 3.5 to 3.75. It can
    also have hilarious outcomes when you get to
    roll a massive amount of dice.  
    """
    res = 0
    while n > 0:
        die = random.randint(1,sides)
        if die == sides and exploding:
            n += 1
            continue
        res += die
        n -= 1
    return res


        
