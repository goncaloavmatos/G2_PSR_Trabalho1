#!/usr/bin/python3
from colorama import Fore, Back, Style
import argparse
import random
import readchar

#Generate lower case character
def randLowercaseChar():
    #ASCII lower case char 'a' and 'z' correspond to decimal 97 and 122, respectively
    n = random.randint(97,122)   #Generate random decimal number between 97 and 122
    c = chr(n) #Turn number into a character
    return c

def NewEntry():


    #Counters for statistical analysis at the end of the test
    countEntry = 0
    countMatch = 0
    countMiss = 0


    while True:

        randC=randLowercaseChar() #Generate new character each loop
        print('Type letter ' + randC) #Ask for letter
        pressed = readchar.readkey() #Save pressed character

        #Abort test if the spacebar is pressed
        if pressed == ' ':
            print(Fore.RED + Style.BRIGHT + Back.YELLOW + 'You pressed the Spacebar. The test stopped.' + Style.RESET_ALL)
            break

        #If the pressed character matches the character that is requested
        if pressed == randC:
            countMatch += 1 #Accumulates match
            countEntry +=1 #Accumulates entry
            print('You typed letter ' + Fore.GREEN + Style.BRIGHT + randC + Style.RESET_ALL)
        else:   #If there is no match
            countMiss += 1 #Accumulate Miss
            countEntry += 1 #Accumulate Entry

            print('You typed ' + Fore.RED + Style.BRIGHT + pressed + Style.RESET_ALL)

        if countEntry == 10:   #If the max value of entries is reached
            print('You typed 10 characters')
            print('Correct: ' + str(countMatch))
            print('Wrong: ' + str(countMiss))
            break


def main():

    print('Press a key to start')

    if readchar.readkey():
        NewEntry()




if __name__ == '__main__':
    main()