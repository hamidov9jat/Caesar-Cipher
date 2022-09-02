from utility import prompt_user, encrypt, decrypt

direction, text, shift = prompt_user()

if direction == 'encode':
    encrypted_text = encrypt(text, shift)
    print(f'The encoded text is {encrypted_text}')
elif direction == 'decode':
    decrypted_text = decrypt(text, shift)
    print(f'The decoded text is {decrypted_text}')

