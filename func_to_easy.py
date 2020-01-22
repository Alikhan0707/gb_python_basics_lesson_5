import json


def write_data_to_file(name, data, new=False, indent=False, to_json=False):
    """
    Write any data to any type of files
    :param name: File name
    :param data: data to write
    :param new: If file is new =True
    :param indent: If you need indent after each line =True
    :param to_json: If you need convert to json file =True
    :return:
    """
    if new and indent:
        with open(name, "w") as f:
            f.write(f"{data}\n")

    elif not new and indent:
        with open(name, "a") as f:
            f.write(f"{data}\n")

    elif new and not indent:
        with open(name, "w") as f:
            f.write(f"{data}")

    elif not new and not indent:
        with open(name, "a") as f:
            f.write(f"{data}")

    elif to_json:
        with open(name, "w") as f:
            json.dump(data, f)


def read_line_by_line(name):
    """
    Read any type of files line by line and return list if lines
    :param name: File name
    :return: list
    """
    try:
        lines_list = []
        with open(name) as f:
            for line in f:
                lines_list.append(line)

        return lines_list

    except FileExistsError:
        print("Directory don't have this file!")

    except FileNotFoundError:
        print("You enter incorrect file name!")


def split_string(string: str):
    """
    Removes all characters and return to you list of str
    :param string: any string
    :return: list
    """
    symbols_list = [":", ";", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "|", "/", "-", "_", "=", "+", "<", ">",
                    ".", ",", "?", "`", "~", "[", "]", "{", "}", " "]

    new_list = string.split()

    last_list = []

    for i in range(len(new_list)):
        for s in symbols_list:

            new_list[i] = new_list[i].strip(s).lower()

    for i in range(len(new_list)):
        for s in symbols_list:
            if s in new_list[i]:
                new_list[i] = new_list[i].strip(s).split(s)

    for i in new_list:

        if type(i) == list:
            for k in i:
                last_list.append(k)

        else:

            last_list.append(i)

#   sum(new_list, []) Не работает

    return last_list


def sum_number_in_list(some_list):
    """
    Return sum of integers in mixed list with stings
    :param some_list: any list
    :return: int
    """

    sum_numbers = 0

    for i in some_list:

        if i.isdigit():

            sum_numbers += int(i)

    return sum_numbers


def translate(dictionary: dict, some_list):

    """
    Translate english words to russian
    :param dictionary: dictionary consist translated words
    :param some_list: list that consist words to translate
    :return: list
    """

    for k, v in dictionary.items():

        for i in range(len(some_list)):

            if some_list[i] == k:

                some_list[i] = dictionary[k]

    return some_list

