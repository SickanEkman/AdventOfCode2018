import sys


set_w_frequencies = set()
counter = 0


def open_file_list():
    with open("utils/Day1_list.txt", "r") as fin:
        data = fin.read()
        return data


def split_numbers(data):
    data_list = data.split("\n")
    return data_list


def count(numbers_list):
    global counter
    for i in numbers_list:
        try:
            counter += int(i)
            check_if_frequency_exist(counter)
        except ValueError:
            pass
    print("Sum:", counter)


def check_if_frequency_exist(frequency):
    global set_w_frequencies
    if frequency in set_w_frequencies:
        print("First duplicate:", frequency)
        sys.exit(0)
    else:
        set_w_frequencies.add(counter)


if __name__ == "__main__":
    numbers = open_file_list()
    l_numbers = split_numbers(numbers)
    while True:
        count(l_numbers)
