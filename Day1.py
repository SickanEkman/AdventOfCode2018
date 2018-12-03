import sys

def open_file_list():
    with open("utils/Day1_list.txt", "r") as fin:
        numbers = fin.read()
        return numbers


def split_numbers(numbers):
    numbers_list = numbers.split("\n")
    return numbers_list


def count(numbers_list):
    counter = 0
    for i in numbers_list:
        try:
            counter += int(i)
        except ValueError:
            pass
    print("Sum:", counter)


def check_duplicates(numbers_list, counter=0):
    set_w_frequencies = set()
    for i in numbers_list:
        if counter in set_w_frequencies:
            print("First duplicate:", counter)
            sys.exit(0)
        else:
            set_w_frequencies.add(counter)
        try:
            counter += int(i)
        except ValueError:
            pass

if __name__ == "__main__":
    numbers = open_file_list()
    numbers_list = split_numbers(numbers)
    count(numbers_list)
    while True:
        check_duplicates(numbers_list)
