from utility import prompt_user, encrypt, decrypt, caesar
from art import logo

while True:
    direction, text, shift = prompt_user()
    caesar(text, shift, direction)

    print('Type "yes" to continue. To stop enter something else')
    ans = input('Do you wanna play again? ').lower()
    if ans in {'yes'}:
        continue
    else:
        break

