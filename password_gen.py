"""Simple password generator"""
import random
from datetime import date


class Passwords:
    no_of_passwords = int(input('How many passwords do you want? '))
    length_of_password = int(input('Password length. e.g 8 characters '))
    choice = str(input(
        '''
    Which type of passwords do you want:
    Enter a for alphabets only:
    Enter b for numbers only:
    Enter c for mixed characters: 
            '''))

    def password_gen(self):
        self.choice
        filemame = 'passwords.txt'

        """ test for exceptions if user is out of range """

        if self.choice == 'a':
            char = "abcdefghijklmnopqrstuvwxyz"
        elif self.choice == 'b':
            char = "0123456789"
        elif self.choice == 'c':
            char = '"<>?,./:";=+-*&$#@!~abcdefghijklmnopqrstuvwxyz0123456789'

        for y in range(self.no_of_passwords):
            password = ''
            for c in range(self.length_of_password):
                password += random.choice(char)
            print(password)

            with open(filemame, 'a') as f:
                f.write(f'{password}\n')





if __name__ == '__main__':
    user = Passwords()
    user.password_gen()
