# Caesar cipher
# List of letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# Main function
def caesar(cipher_direction, start_text, shift_amount):
    if cipher_direction != "encode" and cipher_direction != "decode":
        print("Please enter a valid command.")
    else:
        end_text = ""
        # Deal with shift_amount >= length of the alphabet list
        shift_amount %= len(alphabet)
        for letter in start_text:
            # Deal with non-alphabet character
            if letter not in alphabet:
                end_text += letter
            else:
                # Find the position of character in the alphabet list
                position = alphabet.index(letter)
                # Find the new position
                if cipher_direction == "encode":
                    new_position = position + shift_amount
                    if new_position >= len(alphabet):
                        new_position -= len(alphabet)
                    '''
                    A way in which no need to check the condition: 
                    "double" the alphabet list 
                    check the caesar_ref() for details
                    '''
                if cipher_direction == "decode":
                    new_position = position - shift_amount
                    if new_position < 0:
                        new_position += len(alphabet)
                '''
                Another trick to write the new position finding part: 
                multiply shift by -1 to change the shift direction
                check caesar_ref() for details
                '''
                end_text += alphabet[new_position]
        print(f"The {cipher_direction}d text is {end_text}")


# Reference: a much shorter solution:
alphabet_ref = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_ref(cipher_direction, start_text, shift_amount):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = start_text.index(letter)
        new_position = position + shift_amount
        end_text += alphabet_ref[new_position]
    print(f"The {cipher_direction}d text is {end_text}")


# Play the game
# Greetings
print("Welcome to the Caesar Cipher interpreter ;)")
# Enable to replay the game
replay = "yes"
while replay == "yes":
    # Gather the inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Call the function
    caesar(cipher_direction=direction, start_text=text, shift_amount=shift)
    # Whether to replay
    replay = input("\nRetry? Type 'yes' if you want to go again. Otherwise type 'no'. \n")
