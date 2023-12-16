import string
lower_alphabet, upper_alphabet = list(string.ascii_lowercase), list(string.ascii_uppercase) # establishes the alphabet

def letter_count(file):
    """
    Checks if each character in the file is apart of the alphabet
    If yes, then adds 1 to the letter's value in letter_dict
    """
    f = open(file)
    letter_dict = dict.fromkeys(string.ascii_lowercase, 0) # creates a dictionary with each lowercase letter, starting with the value 0 for each key

    for char in f.read(): # loop that tests every character in the file
        if str(char) in lower_alphabet: # checks if the character is a lowercase letter
            letter_dict[char.lower()] = letter_dict[char] + 1 # adds 1 to the letter's dictionary value
        if str(char) in upper_alphabet: # checks if the character is an uppercase letter
            letter_dict[char.lower()] = letter_dict[char.lower()] + 1 # adds 1 to the letter's dictionary value   
    
    f.close()
    return letter_dict

def letter_frequency(dict_letters):
    """
    Finds the total amount of letters, then calculates each frequency by dividing each dict_letters (or letter_dict) value by the total
    """
    freq_dict = dict.fromkeys(string.ascii_lowercase, 0) # creates a dictionary with each lowercase letter, starting with the value 0 for each key
    total_letters = 0 # establishes a variable with a default empty value that will be updated later

    for letter in dict_letters: # loop that adds each letter count to find total letters
        total_letters = total_letters + int(dict_letters[letter])
    if total_letters > 0: # checks that there are actually letters in the file to avoid division by 0 error
        for letter in dict_letters: # loop that calculates frequency for each letter and replaces each key in freq_dict with the appropriate frequency
            freq_dict[letter.lower()] = (int(dict_letters[letter]) / total_letters)

    return freq_dict

assert(letter_count("frost.txt")["a"] == 13) # tests letter_count function using value from frost.txt given in directions
assert(letter_frequency(letter_count("frost.txt"))["a"] == 0.06190476190476191) # tests letter_frequency function using value from frost.txt given in directions