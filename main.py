#!/usr/bin/python3
from datetime import datetime
from colorama import Fore, Back, Style
from collections import namedtuple
import argparse
import random
import readchar
import time


# =====================================================================================================
# Generate lower case character
# =====================================================================================================
def randLowercaseChar():
    # ASCII lower case char 'a' and 'z' correspond to decimal 97 and 122, respectively

    n = random.randint(97, 122)  # Generate random decimal number between 97 and 122
    c = chr(n)  # Turn number into a character
    return c


# =====================================================================================================
# NEW ATTEMPT FUNCTION
# =====================================================================================================
def NewAttempt(m):
    # Counters for statistical analysis at the end of the test
    countEntry = 0
    countMatch = 0
    countMiss = 0

    #variable with the max value
    MAX = m

    type_average_duration = 0
    type_hit_average_duration = 0
    type_miss_average_duration = 0

    # Elements for the dictionary
    Input = namedtuple('Input', ['requested', 'received', 'duration'])
    Input_list = []


    while True:

        randC = randLowercaseChar()  # Generate new character each loop
        print('Type letter ' + Fore.BLUE + Style.BRIGHT + randC + Style.RESET_ALL)  # Ask for letter

        #o inicio do tempo de teste tem que estar aqui se nao ele inicia quando corres o programa e nao qd inicias o teste
        test_start = datetime.now()  # Save the test start date and time

        sec_start = time.time()
        sec_start_hit = time.time()
        sec_start_miss = time.time()
        pressed = readchar.readkey()  # Save pressed character

        sec_end = time.time()

        dif = sec_end - sec_start


        if type_average_duration == 0:
            type_average_duration = dif
        else:
            type_average_duration = (type_average_duration + dif) / 2

        #print('Time to press key: %3.2f' % dif)  # por so duas casas decimais para o ecra nao ficar muito cheio.

        # Abort the test if the spacebar is pressed
        if pressed == ' ':
            print(
                Fore.RED + Style.BRIGHT + Back.YELLOW + 'You pressed the Spacebar. The test stopped.' + Style.RESET_ALL)
            print('Correct: ' + str(countMatch))
            print('Wrong: ' + str(countMiss))
            break

        # If the pressed character matches the character that is requested
        if pressed == randC:
            sec_end_hit = time.time()
            dif_hit = sec_end_hit - sec_start_hit

            countMatch += 1  # Accumulates match
            countEntry += 1  # Accumulates entry
            print('You typed ' + Fore.GREEN + Style.BRIGHT + randC + Style.RESET_ALL)
            #print('Time to press key: %3.2f' % dif_hit)
            I = Input(randC, pressed, dif)
            Input_list.append(I)

            if type_hit_average_duration == 0:
                type_hit_average_duration = dif_hit
            else:
                type_hit_average_duration = (type_hit_average_duration + dif_hit) / 2

        # If the pressed character does NOT match the character that is requested
        else:
            sec_end_miss = time.time()
            dif_miss = sec_end_miss - sec_start_miss
            #print('Time to press key: %3.2f' % dif_miss)

            countMiss += 1  # Accumulate Miss
            countEntry += 1  # Accumulate Entry

            I = Input(randC, pressed, dif)
            Input_list.append(I)

            print('You typed ' + Fore.RED + Style.BRIGHT + pressed + Style.RESET_ALL)
            if type_miss_average_duration == 0:
                type_miss_average_duration = dif_miss
            else:
                type_miss_average_duration = (type_miss_average_duration + dif_miss) / 2


        if countEntry == MAX:  # If the max value of inputs is reached.
            print(Fore.YELLOW + Style.BRIGHT + '\nTest Finished!\n' + Style.RESET_ALL)
            print('Correct: ' + str(countMatch))
            print('Wrong: ' + str(countMiss))
            break

    test_end = datetime.now() #Save the test end date and time
    test_start_str = test_start.strftime('%a %b %d %H:%M:%S %Y') #Convert the test start date and time to the desired format
    test_end_str = test_end.strftime('%a %b %d %H:%M:%S %Y') #Convert the test end date and time to the desired format
    test_duration = test_end.timestamp() - test_start.timestamp()

    print('\n')
    print('Test duration: %3.2f' % test_duration) #Para testar
    print('Average time to press key: %3.2f' % type_average_duration)
    print('Average time to press wrong key: %3.2f' % type_miss_average_duration)
    print('Average time to press right key: %3.2f' % type_hit_average_duration)
    print('\n')
    print('Test start: ' + test_start_str) #Para testar
    print('Test end: ' + test_end_str) #Para testar
    print('\n')
    #To print list vertically
    for i in range(0,MAX):

        print(Input_list[i])



# =====================================================================================================
# MAIN FUNCTION
# =====================================================================================================
def main():
    # Definition of the arguments that specify how the test will be taken
    parser = argparse.ArgumentParser(description='Definition of test mode.')
    parser.add_argument('-mv', type=int,
                        help='Specify max number of seconds for TIME MODE or max number of inputs for NUMBER OF INPUTS MODE.')
    parser.add_argument('-utm', action='store_true',
                        help='To take the test in TIME MODE or not (Default: NUMBER OF INPUTS MODE).')

    args = vars(parser.parse_args())  # save selected args

    print(Style.BRIGHT + '\n\nTYPE TEST\n' + Style.RESET_ALL)  # Title

    # TO prevent test from starting if a max value isn't specified
    if args['mv'] == None:
        print(Back.RED + 'IMPOSSIBLE TO START. YOU DID NOT INTRODUCE A MAXIMUM VALUE!' + Style.RESET_ALL + '\n')
        exit(0)

    # Test mode selection
    if args['utm']:  # If time mode is selected
        print('You selected ' + Style.BRIGHT + 'TIME MODE.' + Style.RESET_ALL)
        print("You will have to type the maximum amount of letters you can in " + Fore.RED + Style.BRIGHT + str(
            args['mv']) + Style.RESET_ALL + ' seconds.')
        print('\nPress a key to start')

        # If a key is pressed, it starts a new attempt
        if readchar.readkey():
            NewAttempt(args['mv'])  # Starts a new TIME MODE test attempt

    else:  # Default: time mode not selected -> Number of inputs mode
        print('You selected ' + Style.BRIGHT + 'NUMBER OF INPUTS MODE.' + Style.RESET_ALL)
        print("You will have to type " + Fore.RED + Style.BRIGHT + str(
            args['mv']) + Style.RESET_ALL + " letters as quick as you can.")
        print('\nPress a key to start')

        # If a key is pressed, it starts a new attempt
        if readchar.readkey():
            NewAttempt(args['mv'])  # Starts a new NUMBER OF INPUTS MODE test attempt


if __name__ == '__main__':
    main()
