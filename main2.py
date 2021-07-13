"""Reading a file line by line """


def reader():
    filename = 'simple.txt'
    with open(filename) as f:
        for line in f:
            print(line.rstrip())  # removes the empty lines


"""Storing the content in a list"""


def reader_two():
    filename = 'simple.txt'
    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        # print(line.rstrip())
        print(line, end='')


# testing the readline()


def reader_three():
    filename = 'simple.txt'
    with open(filename) as f:
        print(f.readline(10))


if __name__ == "__main__":
    # reader()
    # reader_two()
    reader_three()
