from collections import defaultdict
import sys

twos = 0
threes = 0
list_w_id_sets = []

def open_file_list():
    with open("utils/Day2_list.txt", "r") as fin:
        data = fin.read()
        return data


def split_ids(data):
    data_list = data.split("\n")
    return data_list


def count_letters(data_list):
    for i in data_list:
        my_default_dict = defaultdict(int)
        for c in i:
            my_default_dict[c] = my_default_dict[c] + 1
        count_twos_and_threes(my_default_dict)


def count_twos_and_threes(counting_dict):
    global twos, threes
    if 2 in counting_dict.values():
        twos += 1
    if 3 in counting_dict.values():
        threes += 1


def find_correct_boxes(the_id, l_id):
    for any_id in l_id:
        list_the_id = list(the_id)
        list_any_id = list(any_id)
        counter = 0
        for number in range(26):
            if list_any_id[number] == list_the_id[number]:
                counter += 1
            else:
                pass
        if counter == 25:
            find_shared_letters(list_the_id, list_any_id)

def find_shared_letters(id_one, id_two):
    letters = []
    for number in range(len(id_one)):
        if id_one[number] == id_two[number]:
            letters.append(id_one[number])
        else:
            pass
    print("".join(letters))
    sys.exit(0)


if __name__ == "__main__":
    ids = open_file_list()
    id_list = split_ids(ids)
    count_letters(id_list)
    print("Twos:", twos, "Threes:", threes, "Checksum:", twos * threes)
    for i in id_list:
        find_correct_boxes(i, id_list)
