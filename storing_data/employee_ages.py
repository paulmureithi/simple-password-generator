import json


def ages_writer():
    """writes the ages in a ages.json file"""
    ages = [56, 34, 34, 23, 23, 65, 44, 33, 32, 31, 47, 68]

    filename = 'ages.json'

    with open(filename, 'w') as f:
        json.dump(ages, f)


def ages_reader():
    """reads the ages from the ages.json file"""
    filename = 'ages.json'
    with open(filename) as f:
        ages = json.load(f)

    print(ages)


if __name__ == '__main__':
    ages_writer()
    ages_reader()
