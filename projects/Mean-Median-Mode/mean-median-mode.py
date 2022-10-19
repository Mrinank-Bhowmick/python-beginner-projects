#Asks the user for a series of number and calculates the mean, median, and mode.

import statistics #This is used to find the Median.
from collections import Counter #This is used to find the Mode number(s).

num_list = []
   
def calculate_mean(lst): #Calculates the Mean (or average). Adds all inputs together and divides by the total number of inputs.
    return sum(lst) / len(lst)

def calculate_median(lst): #Calculates the Median. This is the middle number in the sorted list.
    return statistics.median(lst)

def calculate_mode(lst): #Calculates the Mode. This is the most frequent number that appears in the user input.
    c = Counter(lst)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

def ask_for_num(): #Asks user for number.
    print('\nPlease add a new number. Enter C when you want to calculate, or Q to quit.')
    new_num = input()

    if new_num == 'C' or new_num == 'c': #If the user enters C then the calculations are done.
        return evaluate_nums(num_list)
    elif new_num == 'Q' or new_num == 'q': #If the user enters Q then quits the program.
        return ('Thanks, take care!')
    else: #Else if user did not choose C or Q, asks for another number.
        num_list.append(float(new_num))
        print('Your current numbers are:')
        print(num_list)
        return(ask_for_num())

def evaluate_nums(lst): #Evaluates the user's numbers.
    if not lst: #If user didn't enter any numbers yet.
        print("You didn't enter any numbers yet.")
        return(ask_for_num())
    else:
        num_list.sort() #Sort the list from smallest to largest.
        num_mean = calculate_mean(num_list)
        num_median = calculate_median(num_list)
        num_mode = calculate_mode(num_list)

        print(f'\nThe final list is: {num_list}')
        print(f'The Mean, or average is: {num_mean}.')
        print(f'The Median, or middle number is: {num_median}.')
        print(f'The Mode, or most common number(s) is: {num_mode}.')
        return('Thanks!')

# Start of program
print('Calculate the Mean, Median, and Mode of a series of numbers.')
print(ask_for_num()) #Asks user for their first number.