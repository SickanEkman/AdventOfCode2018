import re


def open_file_list():
    with open("utils/Day3_list.txt", "r") as fin:
        data = fin.read()
        return data


def split_claims(data):
    data_list = data.split("\n")
    return data_list


class Claim:
    def __init__(self, claim_info):
        c_info = re.split(',|x|\s', claim_info)
        self.claim_id = c_info[0]
        self.dist_left = c_info[2]
        self.dist_top = c_info[3]
        self.width = c_info[4]
        self.hight = c_info[5]


if __name__ == "__main__":
    claim_data = open_file_list()
    claims = split_claims(claim_data)
    for c in claims:
        claim_object = Claim(c)
