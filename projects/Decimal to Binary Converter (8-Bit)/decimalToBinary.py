'''
Purpose: Convert a decimal number from 0 to 255 to binary. (8-bit conversion)
Author: VladinXXV
Date: October 24, 2022
'''

def convertToBinary(decimal):
    '''Converts a given integer between 0 and 255 (including ends) to binary.

    Parameters:
        decimal: String of an integer between 0 and 255 (including ends) to convert.

    Return value:
        Binary represenation of the integer as a string OR None if the input wasn't good.
    '''
    
    #If the input is bad, tell the user and return.
    if (decimal < 0) or (decimal > 255) or (isinstance(decimal, int) == False):
        print("ALERT: Please enter an integer that is between 0 and 255, including endpoints.")
        return

    #For 8-bit, k starts at 7. Binary is our default binary output.
    binary = '00000000'
    k = 7 #Used as 2^k

    #While decimal is greater than 0...
    while decimal > 0:
        #If 2^k is greater than the decimal, subtract 1 from k. Else..
        if (2**k) > decimal:
            k = k - 1
        #If decimal - 2^k is greater than or equal to 0...
        elif decimal - (2**k) >= 0: 
            decimal = decimal - (2**k) #Subtract 2^k from decimal
            binary = binary[::-1] #Reverse the order of binary
            binaryList = list(binary) #Make it a list
            binaryList[k] = '1' #Replace the kth character with 1
            binary = ''.join(binaryList)[::-1] #Reverse again and join into a string

        #Else, just subtract 1 from k.
        else:
            k = k - 1
            
    #Return the output.
    return binary

def main():
    '''Ask the user for input, print result.
    '''

    #Forever...
    while True:
        #Get the decimal number
        decimal = input("Enter an integer between 0 and 255 (including endpoints): ")

        #Try to convert to integer...
        try:
            decimal = int(decimal)
        #Don't try and give me text or something.
        except:
            print("ALERT: Please enter an integer.")
            continue
        
        #Convert to binary
        binary = convertToBinary(decimal)

        #Don't print anything else if the number was too large
        if binary == None:
            continue
        else:
            #Print the result.
            print("The number", str(decimal), "is", binary, "in binary.")

        #Ask if we keep going..
        choice = input("Continue? Y/N: ")
        #If yes, keep it going.
        if choice == 'Y' or choice == 'y':
            continue
        #If no, stop.
        elif choice == 'N' or choice == 'n':
            return

#So it can be standalone or imported.
if __name__ == '__main__':
    main()
