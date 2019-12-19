import time
import random


def printing(message):
    print(f'{message}\n')
    time.sleep(1)


def choose_again():
    printing("Please enter 1 or 2.")


def won():
    printing('You have kill the zombie. You are safe!')
    printing("You won! Thank you for playing")
    play_again()


def loose():
    printing("You don't have a gun! You can't protect yourself. You die!!")
    printing("You loose! Thank you for playing")
    play_again()


def play_again():
    printing("Do you wish to play again?")
    choice = input("Enter yes or no:\n").lower()
    if choice == 'yes':
        printing("Restarting Game")
        game()
    elif choice == 'no':
        printing("See you next time")
    else:
        play_again()


def house(items):
    sizes = ['big', 'medium', 'small']
    size = random.choice(sizes)
    printing("You are in house")
    printing(f"Suddenly you see a {size} zombie.")
    while True:
        choice = input("Enter 1 to fight.\nEnter 2 to run away.\n")
        if choice == '1':
            if 'gun' in items:
                won()
                break
            else:
                loose()
                break
        if choice == '2':
            if 'gun' in items:
                printing("You are running away, next time  use gun!")
                field(items)
            else:
                printing("You are running away back into the field!")
                printing("Maybe go look for guns")
                field(items)
            break
        else:
            choose_again()


def shed(items):
    leave = "There is nothing more in the shed, you go out into the field"
    printing('You are in shed')
    if 'gun' in items:
        printing("There is nothing else to see in the shed")
        field(items)
    else:
        printing("You have spotted a gun! What will you do?!")
        while True:
            choice = input(
                'Enter 1 to take the gun.\nEnter 2 to leave the gun\n')
            if choice == '1':
                printing("Good, now you can defend yourself")
                printing(leave)
                items.append('gun')
                field(items)
                break
            elif choice == '2':
                printing("Maybe you do not need the fun after all..")
                printing(leave)
                field(items)
                break
            else:
                choose_again()


def field(items):
    message = "Enter 1 to go inside the house.\nEnter 2 to go to the shed.\n"
    while True:
        choice = input(message)
        if choice == '1':
            house(items)
            break
        elif choice == '2':
            shed(items)
            break
        else:
            choose_again()
    pass


def intro():
    printing("You find yourself in the zombie apocalypse.")
    printing("In front of you are two passageways.")


def game():
    items = []
    intro()
    field(items)


game()
