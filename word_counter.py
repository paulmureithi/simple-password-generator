"""a python script for counting number of words in a document"""


def words_counter():
    filenames = []
    print('This app counts the number of words in your documents')

    while True:
        users_files = str(input('Enter name of document\n'))
        filenames.append(users_files)
        add_file = str(input('Add another doc? Y for YES N for NO'))

        if add_file.upper() == 'Y':
            continue
        else:
            break

    for doc in filenames:

        try:
            with open(doc) as f:
                content = f.read()
        except FileNotFoundError:
            print(f'Sorry the file {doc} cannot be found.')
        else:
            words = content.split()
            num_of_words = len(words)
            print(f'The document {doc} has {num_of_words} words.')


if __name__ == "__main__":
    words_counter()
