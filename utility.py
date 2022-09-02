from string import ascii_lowercase

NUM_OF_LETTERS = len(ascii_lowercase)
alphabet = dict(zip(ascii_lowercase, range(NUM_OF_LETTERS)))


def prompt_user():

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    while direction not in {'encode', 'decode'}:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    return direction, text, shift


def encrypt(text, shift):
    encrypted_text = ''

    for character in text:
        if character.isalpha():
            index_of_changed = (alphabet[character] + shift) % NUM_OF_LETTERS
            encrypted_character = ascii_lowercase[index_of_changed]
            encrypted_text += encrypted_character
        else:
            encrypted_text += character

    return encrypted_text


def decrypt(encrypted_text, shift):
    decrypted_text = ''

    for character in encrypted_text:
        if character.isalpha():
            index_of_changed = (alphabet[character] - shift) % NUM_OF_LETTERS
            decrypted_character = ascii_lowercase[index_of_changed]
            decrypted_text += decrypted_character
        else:
            decrypted_text += character

    return decrypted_text


def caesar(text, shift, direction):
    if direction == 'encode':
        encrypted_text = encrypt(text, shift)
        print(f'The encoded text is {encrypted_text}')
    elif direction == 'decode':
        decrypted_text = decrypt(text, shift)
        print(f'The decoded text is {decrypted_text}')


if __name__ == '__main__':
    print(encrypt('abc', 1))
    print(decrypt('abc', 1))
