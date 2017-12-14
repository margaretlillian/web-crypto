alphabet = "abcdefghijklmnopqrstuvwxyz"

def rotate_character(char, rot):
    rotation = (alphabet_position(char) + rot) % 26
     # allows user to enter numbers larger than 26
    if char.isupper():
        return alphabet[rotation].upper() #Keep uppercase uppercase
    else:
        return alphabet[rotation] 

def alphabet_position(letter):
    new_letter = letter.lower() # to ignore case
    return alphabet.index(new_letter) #Get each letters position in the alphabet