from helpers import rotate_character, alphabet_position

def caesar_rotate_string(text, rot):
    letter_str = ''
    for char in text:
        if char.isalpha():
            letter_str += rotate_character(char, rot)
        else:
            letter_str += char    
    return letter_str   

def vigenere_rotate_string(text, rot):
    letter_str = ''
    counter = 0 
    for char in text:
        key_list = []
        for chars in rot:
            key_list.append(alphabet_position(chars)) #create a list of rotations 
        if char.isalpha():
            # Iterates through list of rotations, "skipping over" spaces, punctuation, etc. 
            letter_str += rotate_character(char, key_list[counter % len(key_list)])
            counter += 1
        else: 
            letter_str += char
    return letter_str