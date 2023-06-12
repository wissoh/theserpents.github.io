import random

def draw_dice(dice_value):
    if dice_value == 1:
        print("+---------+")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("+---------+")
    elif dice_value == 2:
        print("+---------+")
        print("| O       |")
        print("|         |")
        print("|       O |")
        print("+---------+")
    elif dice_value == 3:
        print("+---------+")
        print("| O       |")
        print("|    O    |")
        print("|       O |")
        print("+---------+")
    elif dice_value == 4:
        print("+---------+")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print("+---------+")
    elif dice_value == 5:
        print("+---------+")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print("+---------+")
    elif dice_value == 6:
        print("+---------+")
        print("| O     O |")
        print("| O     O |")
        print("| O     O |")
        print("+---------+")

def roll_dice():
    # Generate random numbers between 1 and 6 for two dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    # Calculate the total sum of the dice
    total = dice1 + dice2
    
    # Print the results and draw the dice
    print("Dice 1:")
    draw_dice(dice1)
    print()
    print("Dice 2:")
    draw_dice(dice2)
    print()
    print("Total:", total)

# Main program
print("Roll the Dice")
print("----------------")
roll_dice()
