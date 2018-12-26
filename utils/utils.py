
def open_file(filename):
    with open(filename, "r") as fin:
        data = fin.read()
        return data


def string_to_list(data):
    data_list = data.split("\n")
    return data_list
