from collections import defaultdict
import sys
from utils.utils import open_file, string_to_list


twos = 0
threes = 0
list_w_id_sets = []
width_of_codes = 26


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


# todo: byt namn så det blir tydligare vad funktionen gör
def find_correct_boxes(the_id, l_id):
    for any_id in l_id:
        list_the_id = list(the_id)
        list_any_id = list(any_id)
        counter = 0
        # todo: lägg jämförelseraderna i egen metod
        for number in range(width_of_codes):
            # TODO: Hoppa över det egna id:t (the_id)
            if list_any_id[number] == list_the_id[number]:
                counter += 1
            else:
                pass
        if counter == (width_of_codes - 1):
            find_shared_letters(list_the_id, list_any_id)


# todo: byt namn så det blir tydligare vad funktionen gör
def find_shared_letters(id_one, id_two):
    letters = []
    for number in range(len(id_one)):
        if id_one[number] == id_two[number]:
            letters.append(id_one[number])
        else:
            pass
    print("".join(letters))
    # todo: lägg detta i main. Returnera hellre ett värde.
    sys.exit(0)


if __name__ == "__main__":
    ids = open_file("utils/Day2_list.txt")
    id_list = string_to_list(ids)
    count_letters(id_list)
    print("Twos:", twos, "Threes:", threes, "Checksum:", twos * threes)
    for x in id_list:
        find_correct_boxes(x, id_list)
