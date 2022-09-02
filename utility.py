from string import ascii_lowercase

NUM_OF_LETTERS = len(ascii_lowercase)
alphabet = dict(zip(ascii_lowercase, range(NUM_OF_LETTERS)))


def prompt_user():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    return (direction, text, shift)


def encrypt(text, shift):
    encrypted_text = ''

    for character in text:
        if str.isalpha():
            index_of_changed = (alphabet[character] + shift) % NUM_OF_LETTERS
            encrypted_character = ascii_lowercase[index_of_changed]
            encrypted_text += encrypted_character
        else:
            encrypted_text += character

    return encrypted_text



if __name__ == '__main__':
    pass
