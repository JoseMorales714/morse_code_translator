 MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'}

def encrypt(message):
    cipher = '' #traverses the string and matches it with the morse code
    for letter in message:
        if letter != ' ': #match with letter if no space
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' ' #a new word is detected from extra space
    return cipher

def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        # checks for space and keep count
        if (letter != ' '):
            i = 0
            citext += letter # storing morse code of a single character
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2 :
                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''

    return decipher

def main():
    message = input("Enter your message") #message input from user
    result = encrypt(message.upper())
    print (result)

if __name__ == '__main__':
    main()