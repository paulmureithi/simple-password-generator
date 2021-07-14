"""returns total of marks entered"""


def sum_marks():
    print('Returns total of marks entered')
    total = 0
    count = 0

    while True:
        try:
            score = int(input("Enter your score:"))
            total += score
            count += 1
            average = round(total/count, 2)
        except ValueError:
            print('Score should be an integer')
            continue
        else:
            print(f'Total is: {total}. Average for the {count} scores is: {average}.')
            quit = str(input('Add another score? Y for YES N for NO'))

        if quit.upper() == 'Y':
            continue
        else:
            break


if __name__ == "__main__":
    sum_marks()