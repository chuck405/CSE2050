import letters

def highest_freq(file):
    """
    Tests if the frequency of each letter is greater than the previous highest frequency
    If yes, then updates that letter's frequency to be the new highest
    (In the instance that 2 letter's frequencies are tied, it will only return the frequency of the first alphabetical letter)
    """
    highest_letter, highest = None, 0 # establishes a variable pair with default empty values that will be updated later on

    for letter in letters.letter_frequency(letters.letter_count(file)):
        if letters.letter_frequency(letters.letter_count(file))[letter] > highest: # checks if the current letter's frequency is greater than the current highest frequency
            highest_letter, highest = letter, letters.letter_frequency(letters.letter_count(file))[letter] # updates the new "highest_letter, highest" pair

    return highest_letter, highest

assert(highest_freq("frost.txt") == ("e", 0.10952380952380952)) # tests highest_freq function using value from frost.txt given in directions