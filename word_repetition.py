"""counts the number of times a word is repeated in a text document"""


def word_counter(filename, word):
    print(f"Counts how many times the word {word} is repeated in a text")

    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        print(f'Sorry the doc {filename} is not available. Please check the spelling.')
    else:
        repeated_times = content.lower().count(word)
        print(f"The word '{word}' is repeated {repeated_times} times in {filename}")


if __name__ == '__main__':
    document = str(input('Enter filename: \n'))
    word_to_check = str(input('Enter the word: \n'))
    word_counter(document, word_to_check)