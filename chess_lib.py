from colorama import Fore, Back
from os import system
from time import sleep

def clear():
    system('clear')

def print_chess_table(tokens_characteristics):
    
    clear()

    size_of_chess_table = [8, 8]

    for line in range(size_of_chess_table[1]):

        for frame_line in range(4):

            for column in range(size_of_chess_table[0]):

                if (line % 2 == column % 2):
                    print(Back.GREEN + "", end="")
                else:
                    print(Back.BLACK + "", end="")

                print(" " * 8, end="")

            print(Back.RESET + "")

if __name__ == '__main__':
    pass