# Caesar Cipher
import string

alphabet = list(string.ascii_lowercase)

def caesar(original_text, shift_amount, encode_decode):
    output_text = ""
    for letter in original_text:

        if letter not in alphabet:
            output_text +=letter
        else:
            if encode_decode == "encode":
                shifted_position = alphabet.index(letter) + shift_amount
            elif encode_decode == "decode":
                shifted_position = alphabet.index(letter) - shift_amount
            
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_decode}d result: {output_text}")

further = True

while further:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input('Type "yes" if you want to go again. Otherwise, type "no".\n').lower()
    if  restart == "no":
        further = False
        print("Goodbye!")
