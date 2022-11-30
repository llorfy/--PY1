import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimiter = ',', new_line = "\n") -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json
    with open(filename, encoding="utf-8") as input_file:
        list_ = []
        for line_ in input_file:
            list_.append([x.rstrip(new_line) for x in line_.split(delimiter)])

    list_dict = []
    for i in range(1, len(list_)):
        dict_ = {}
        for j in range(len(list_[0])):
            dict_.update({list_[0][j]: list_[i][j]})
        list_dict.append(dict_)

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
