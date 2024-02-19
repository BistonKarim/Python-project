
# this function takes tow string as input and return the shared character
def shared_characters(string1, string2):
    string1 = string1.lower() # If the user print a uppercase letters so this function will convert it to lower case
    string2 = string2.lower()

    shared = ""
    for char in string1:
        if char in string2 and char not in shared:
            shared += char 
              
    # convert the shared string to a list and sorting the result so that the letters are in order
    # and join it back into a string     
    theList = list(shared)
    theList.sort()
    sortList = " , " .join(theList)
    return sortList


# This function takes two strings as input and returns the unique characters
def unique_characters(string1, string2):
    string1 = string1.lower() # If the user print a uppercase letters so this function will convert it to lower case
    string2 = string2.lower()
    unique = ""
    for char in string1 + string2:
        if char not in string1 or char not in string2:
            if char not in unique:
                unique += char
    
    # convert the shared string to a list and sorting the result so that the letters are in order            
    # and join it back into a string 
    theList = list(unique)
    theList.sort()
    sortedlist = " , " .join(theList)
    return sortedlist

# This function takes two strings as input and returns the letters of the alphabetb
# that dont occur in either string in sorted order
def non_ccurring_alphabet_letters(string1, string2):
    string1 = string1.lower() # If the user print a uppercase letters so this function will convert it to lower case
    string2 = string2.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    non_curring = "" 
    for char in alphabet:
        if char not in string1 and char not in string2:
            non_curring += char 
    # convert the shared string to a list and sorting the result so that the letters are in order
    # and join it back into a string 
    theList = list(non_curring)
    theList.sort()
    sortedlist = " , " .join(theList)
    return sortedlist

            
    
# in main function call we for all the functions
def main():
    first_string = input("Enter the first string: ")
    secound_string = input("Enter the second string: ")
    
    shared = shared_characters(first_string, secound_string )
    print(shared, "\n")
    
    
    unique = unique_characters(first_string, secound_string)
    print(unique, "\n")
    
    nonCurreing = non_ccurring_alphabet_letters(first_string, secound_string)
    print(nonCurreing, "\n")
    
main()
