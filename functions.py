FILEPATH = "text.txt"


def get_list(filepath=FILEPATH):
    new_list = []
    with open(filepath, "r") as f:
        lines = f.readlines()
        for line in lines:
            new_list.append(line)
    return new_list


