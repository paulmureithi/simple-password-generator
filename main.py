def read_files():
    with open('simple.txt') as f:
        content = f.read()
        print(content)


if __name__ == '__main__':
    read_files()