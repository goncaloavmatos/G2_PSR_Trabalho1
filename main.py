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

def NewAttempt(m):


    #Counters for statistical analysis at the end of the test
    countEntry = 0
    countMatch = 0
    countMiss = 0
    MAX = m

    while True:

        randC=randLowercaseChar() #Generate new character each loop
        print('Type letter ' + Fore.BLUE + Style.BRIGHT + randC + Style.RESET_ALL) #Ask for letter
        pressed = readchar.readkey() #Save pressed character

        pressed_keys = []  # empty list to start

        #Abort the test if the spacebar is pressed
        if pressed == ' ':
            print(Fore.RED + Style.BRIGHT + Back.YELLOW + 'You pressed the Spacebar. The test stopped.' + Style.RESET_ALL)
            print('Correct: ' + str(countMatch))
            print('Wrong: ' + str(countMiss))
            break

        #If the pressed character matches the character that is requested
        if pressed == randC:
            countMatch += 1 #Accumulates match
            countEntry +=1 #Accumulates entry
            print('You typed ' + Fore.GREEN + Style.BRIGHT + randC + Style.RESET_ALL)
        else:   #If there is no match
            countMiss += 1 #Accumulate Miss
            countEntry += 1 #Accumulate Entry

            print('You typed ' + Fore.RED + Style.BRIGHT + pressed + Style.RESET_ALL)

        if countEntry == MAX:   #If the max value of inputs is reached
            print('Correct: ' + str(countMatch))
            print('Wrong: ' + str(countMiss))
            break


def main():

    parser = argparse.ArgumentParser(description='Definition of test mode.')
    parser.add_argument('-MV', type=int, help='Specify max number of seconds for TIME MODE or max number of inputs for NUMBER OF INPUTS MODE ')
    parser.add_argument('-utm', action='store_true', help='To take the test in time mode or not')

    args = vars(parser.parse_args())

    print(Style.BRIGHT  + 'TYPE TEST' + Style.RESET_ALL)

    #Choice of the test mode
    if args['utm']:
        print('You requested ' + Style.BRIGHT +  'TIME MODE.' + Style.RESET_ALL )
        print("You will have to type the maximum amount of letters you can in " + Fore.RED + Style.BRIGHT+ str(args['MV']) +  Style.RESET_ALL + ' seconds')
    else:
        print('You requested ' + Style.BRIGHT + 'NUMBER OF INPUTS MODE.' + Style.RESET_ALL )
        print("You will have to type " + Fore.MAGENTA + Style.BRIGHT+ (args['MV']) + Style.RESET_ALL + " letters as quick as you can")


    print('Press a key to start')

    #If a key is pressed, it starts a new attempt
    if readchar.readkey():
        NewAttempt(args['MV'])




if __name__ == '__main__':
    main()