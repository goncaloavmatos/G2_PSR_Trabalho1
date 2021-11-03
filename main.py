#!/usr/bin/python3

from colorama import Fore, Back, Style
from collections import namedtuple
import argparse
import random
import readchar
import time
from pprint import pprint


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
def NewAttempt(m, start, mode):
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


        sec_start = time.time()
        sec_start_hit = time.time()
        sec_start_miss = time.time()
        pressed = readchar.readkey()  # Save pressed character

        sec_end = time.time()


        dif = sec_end - sec_start

        #Calcular média de tempo de resposta
        if type_average_duration == 0:
            type_average_duration = dif
        else:
            type_average_duration = (type_average_duration + dif) / 2

        # print('Time to press key: %3.2f' % dif)  # codigo %3.2f é para por duas casas decimais

        # Abort the test if the spacebar is pressed
        if pressed == ' ':
            print('\n' +Fore.RED + Style.BRIGHT + Back.YELLOW + 'You pressed the Spacebar. The test stopped.' + Style.RESET_ALL + '\n')
            exit(0)

        time_now = time.time()
        duration = time_now - start



        # ===========================================================================================================
        # CORRECT PRESS: If the pressed character matches the character that is requested


        if pressed == randC:
            sec_end_hit = time.time()
            dif_hit = sec_end_hit - sec_start_hit

            countMatch += 1  # Accumulates match
            countEntry += 1  # Accumulates entry

            if duration > MAX and mode == 1:
                print('\n\n')  #imprimir espaços para destacar letra premida depois do tempo
                countMatch -= 1  # Accumulates match
                countEntry -= 1  # Accumulates entry

            print('You typed ' + Fore.GREEN + Style.BRIGHT + randC + Style.RESET_ALL)
            #print('Time to press key: %3.2f' % dif_hit)
            I = Input(randC, pressed, dif)
            Input_list.append(I)

            if type_hit_average_duration == 0:
                type_hit_average_duration = dif_hit
            else:
                type_hit_average_duration = (type_hit_average_duration + dif_hit) / 2


        # ===========================================================================================================
        # WRONG PRESS: If the pressed character does NOT match the character that is requested


        else:
            sec_end_miss = time.time()
            dif_miss = sec_end_miss - sec_start_miss
            #print('Time to press key: %3.2f' % dif_miss)

            countMiss += 1  # Accumulate Miss
            countEntry += 1  # Accumulate Entry

            if duration > MAX and mode == 1:
                print('\n\n')  #imprimir espaços para destacar letra premida depois do tempo
                countMiss -= 1  # Accumulate Miss
                countEntry -= 1  # Accumulate Entry


            I = Input(randC, pressed, dif)
            Input_list.append(I)

            print('You typed ' + Fore.RED + Style.BRIGHT + pressed + Style.RESET_ALL)
            if type_miss_average_duration == 0:
                type_miss_average_duration = dif_miss
            else:
                type_miss_average_duration = (type_miss_average_duration + dif_miss) / 2


        # ===========================================================================================================
        # CONDITIONS TO STOP TEST
        # ===========================================================================================================
        # Conditions to stop test in NUMBER OF INPUTS MODE
        # First: be in NUMBER OF INPUTS MODE; Second: number of inputs equal to max value

        if (mode == 0) and countEntry == MAX:  # Conditions to stop test in NUMBER OF INPUTS MODE

            print(Fore.YELLOW + Style.BRIGHT + '\nTest Finished!\n' + Style.RESET_ALL)

            #for i in range(0, MAX):
            #    print(Input_list[i])
            #    test_end = datetime.now()  # Save the test end date and time
            break

        # ===========================================================================================================
        # Conditions to stop test in TIME MODE
        # First: be in TIME MODE; Second: test time bigger than max value

        if (mode == 1) and duration >= MAX:
            print(Fore.LIGHTRED_EX + Style.BRIGHT + 'Last type did not count because it was made after ' + str(MAX) + ' seconds.' + '\n' + Style.RESET_ALL)
            print(Fore.YELLOW + Style.BRIGHT + '\nTest Finished!\n' + Style.RESET_ALL)

            #test_end = datetime.now()  # Save the test end date and time
            break


    test_end = time.ctime(time_now)
    test_start = time.ctime(start)

    print(Style.BRIGHT + '\nRESULTS AND STATISTICS' + Style.RESET_ALL)


    # Dicionário
    Dictionary = {'accuracy': countMatch / countEntry,
                  'inputs': Input_list,
                  'number_of_hits': countMatch,
                  'number_of_types': countEntry,
                  'test_duration': duration,
                  'test_end': test_end,
                  'test_start': test_start,
                  'type_average_duration': type_average_duration,
                  'type_hit_average_duration': type_hit_average_duration,
                  'type_miss_average_duration': type_miss_average_duration}
    pprint(Dictionary)
    print('\n')



# =====================================================================================================
# MAIN FUNCTION
# =====================================================================================================
def main():

    # Definition of the arguments that specify how the test will be taken
    parser = argparse.ArgumentParser(description='Definition of test mode.')
    parser.add_argument('-mv', '--max_value', type=int,
                        help='Specify max number of seconds for TIME MODE or max number of inputs for NUMBER OF INPUTS MODE.')

    parser.add_argument('-utm', '--use_time_mode', action='store_true',
                        help='To take the test in TIME MODE or not (Default: NUMBER OF INPUTS MODE).')

    args = vars(parser.parse_args())  # save selected args

    #igualar mv e max_value e os mesmo para utm
    args['mv'] = args ['max_value']
    args['utm'] = args['use_time_mode']

    print(Style.BRIGHT + '\n\nTYPE TEST\n' + Style.RESET_ALL)  # Title

    # To prevent test from starting if a max value isn't specified
    if (args['mv']) == None:
        print(Back.RED + 'IMPOSSIBLE TO START. YOU DID NOT INTRODUCE A MAXIMUM VALUE!' + Style.RESET_ALL + '\n')
        exit(0)

    if (args['max_value']) == None:
        print(Back.RED + 'IMPOSSIBLE TO START. YOU DID NOT INTRODUCE A MAXIMUM VALUE!' + Style.RESET_ALL + '\n')
        exit(0)

    # Test mode selection
    if args['utm']:  # If time mode is selected
        time_mode = 1
        print('You selected ' + Style.BRIGHT + 'TIME MODE.' + Style.RESET_ALL)
        print("You will have to type the maximum amount of letters you can in " + Fore.RED + Style.BRIGHT + str(
            args['mv']) + Style.RESET_ALL + ' seconds.')
        print('\nPress a key to start')


    else:  # Default: time mode not selected -> Number of inputs mode
        time_mode = 0
        print('You selected ' + Style.BRIGHT + 'NUMBER OF INPUTS MODE.' + Style.RESET_ALL)
        print("You will have to type " + Fore.RED + Style.BRIGHT + str(
            args['mv']) + Style.RESET_ALL + " letters as quick as you can.")
        print('\nPress a key to start')


    if readchar.readkey():
        test_start = time.time()  # Save the test start date and time
        NewAttempt(args['mv'], test_start, time_mode)  # Starts a new NUMBER OF INPUTS MODE test attempt


if __name__ == '__main__':
    main()

