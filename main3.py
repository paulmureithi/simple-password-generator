"""writing to files"""


def bio():
    filename = 'mybio.txt'
    with open(filename, 'w') as f:
        f.write('Ladies and gentlemen, a short story about me...')


def your_bio():
    filename = 'user.txt'
    user = input('Describe yourself in 5 words...')
    with open(filename, 'w') as f:
        f.write(user)


def guests():
    filename = 'guest_book.txt'
    count = 0

    while True:
        name = input("Your name please: \n")
        with open(filename, 'a') as f:
            f.write(f'{count}. {name} \n')
            count += 1
            question = input('Register another guest? y/n')
            if question.lower() == 'y':
                continue
            break


if __name__ == '__main__':
    # bio()
    # your_bio()
    guests()