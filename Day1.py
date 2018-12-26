import sys
from utils.utils import open_file, string_to_list


set_w_frequencies = set()
counter = 0


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
    numbers = open_file("utils/Day1_list.txt")
    l_numbers = string_to_list(numbers)
    while True:
        count(l_numbers)
