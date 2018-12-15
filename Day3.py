import re


claim_dict = {}
claimed_inch = set()
double_claimed_inch = set()

def open_file_list():
    with open("utils/Day3_list.txt", "r") as fin:
        data = fin.read()
        return data


def string_to_list(data):
    data_list = data.split("\n")
    return data_list


class Claim:
    def __init__(self, claim_info):
        c_info = self.clean_claim_info(claim_info)
        self.claimed_inches = []
        self.claim_id = int(c_info[0])
        self.dist_left = int(c_info[1])
        self.dist_top = int(c_info[2])
        self.width = int(c_info[3])
        self.height = int(c_info[4])
        self.list_claimed_inches()

    @staticmethod
    def clean_claim_info(claim):
        claim_no_at = claim.replace("@", "")
        claim_no_colon = claim_no_at.replace(":", "")
        claim_no_comma = claim_no_colon.replace(",", " ")
        claim_no_hashtag = claim_no_comma.replace("#", "")
        claim_no_x = claim_no_hashtag.replace("x", " ")
        claim_no_double_space = claim_no_x.replace("  ", " ")
        c_info = claim_no_double_space.split(" ")
        return c_info

    def list_claimed_inches(self):
        horiz_list = []
        vert_list = []
        for n in range(self.width):
            horiz_list.append(self.dist_left + n + 1)
        for n in range(self.height):
            vert_list.append(self.dist_top + n + 1)
        for h_point in horiz_list:
            for v_point in vert_list:
                self.claimed_inches.append((h_point, v_point))


def add_object_to_dict(obj):
    claim_dict[obj.claim_id] = obj


def register_claimed_inches(obj):
    for square_inch in obj.claimed_inches:
        if square_inch not in claimed_inch:
            claimed_inch.add(square_inch)
        else:
            double_claimed_inch.add(square_inch)


if __name__ == "__main__":
    claim_data = open_file_list()
    claim_list = string_to_list(claim_data)
    for c in claim_list:
        claim_object = Claim(c)
        register_claimed_inches(claim_object)
    print(claimed_inch)
    print(double_claimed_inch)
