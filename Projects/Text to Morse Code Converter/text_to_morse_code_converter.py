# Text to Morse Code Converter

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def text_to_morse_code(message):
    output_text = ""
    for letter in message:
        if letter != " ":
            output_text += MORSE_CODE_DICT[letter] + " "
        else:
            output_text += "   "
    print(output_text)

def find_key_by_value(dict, morse_letter):
    for k, v in dict.items():
        if v == morse_letter:
            return k
    return None

def morse_code_to_message(morse_message):
    output_text = ""

    words = morse_message.split("   ")

    for word in words:
        letters = word.split(" ")
        for letter in letters:
            if letter:
                output_text += find_key_by_value(MORSE_CODE_DICT, letter)
        output_text += " "

    print(output_text.strip())


working = True

while working:
    print("Option 1: translate Englisch to Morse Code")
    print("Option 2: translate Morse Code to Englisch")
    print("To stop a programm, enter 'STOP'")

    option = input("Enter an option: ").upper().strip()

    if option == "STOP":
        working = False
    
    elif option != "STOP" and option == "1":
        text = input("Enter text: \n").upper().strip()
        text_to_morse_code(text)

    elif option != "STOP" and option == "2":
        morse = input("Enter morse code: \n").strip()
        morse_code_to_message(morse)

    else:
        pass
