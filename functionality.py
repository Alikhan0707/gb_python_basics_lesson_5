# Exercise #1


def open_write_to_file(name, mode, data, indent=False):
    """
    Opens file to reading and writing data.
    modes:
    'r' – Read mode which is used when the file is only being read
    'w' – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
    'a' – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
    'r+' – Special read and write mode, which is used to handle both actions when working with a file
    :param name: file name
    :param mode: mode of open
    :param data: the data you want to write to the file
    :param indent: line indent (default value is 'False')
    """

    if indent:

        with open(name, mode) as f:
            f.write(f"{data}\n")

    else:

        with open(name, mode) as f:
            f.write(f"{data}")


# Exercise #2


def count_lines_and_simbols(name):

    list_line_len = []

    try:
        with open(name) as f:

            for line in f:

                list_line_len.append(len(line))

    except FileNotFoundError:
        print("You enter incorrect name file")
    return list_line_len


# Exercise #3


def workers_data(name):

    """
    Return workers data dictionary
    :param name: file name
    :return: workers dictionary
    """

    workers_dict = {}

    try:

        with open(name) as f:

            for line in f:

                split_line = line.split(":")
                workers_dict[split_line[0]] = split_line[1]

    except FileNotFoundError:
        print("You enter incorrect name file")

    return workers_dict


# Exercise #4


def translate_words(name):
    """
    Translate english words to russian
    :param name: file name
    :return: new list with translation
    """
    trans_words_dict = {"one": "один", "two": "два", "three": "три", "four": "четыре"}
    lines_list = []
    try:
        with open(name) as f:
            for line in f:
                split_line = line.split(" - ")
                new_line = f"{trans_words_dict[split_line[0]] - split_line[1]}"
                lines_list.append(new_line)

    except FileNotFoundError:
        print("You enter incorrect name file")

    return lines_list


# Exercise #5


def new_file_with_data(name, mode, data):

    """
    Create new file and write some data
    :param name: new file name
    :param mode: mode of open
    :param data: that data you want to write to new file
    :return:
    """

    try:

        with open(name, mode) as f:
            f.write(data)

    except IOError:
        print("Some error")


def read_and_sum(name):
    """
    Read data and sum numbers in file
    :param name: file name
    :return: sum of list
    """
    numbers_list = []
    try:
        with open(name) as f:
            for line in f:
                split_line = line.split()
                numbers_list.append(split_line)
    except FileNotFoundError:
        print("You enter incorrect name file")

    return sum(numbers_list)


# Exercise #6


def lessons(name):
    """
    Slit the string data and sum numbers
    :param name: file name
    :return: return dictionary of data
    """
    lessons_dict = {}
    try:

        with open(name) as f:
            for line in f:
                sp_first = line.split(":")
                sp_second = sp_first[1].split()
                lessons_dict[sp_first[0]] = 0
                for i in sp_second:
                    if "(" in i:
                        sp_third = i.split("(")
                        lessons_dict[sp_first[0]] += int(sp_third[0])
    except FileNotFoundError:
        print("You enter incorrect name file")

    return lessons_dict


# Exercise #7


def list_of_companies(name):

    list_comp = []
    comp_dict = {}
    average = {"average_profit": 0}
    try:

        with open(name) as f:

            for line in f:

                sp_line = line.split()

                comp_dict[sp_line[0]] = 0

                for i in sp_line:
                    for k in range(10):
                        if str(k) in i:

                            comp_dict[sp_line[0]] += int(i)

        list_comp.append(comp_dict)
        for k, v in comp_dict.items():
            if v > 0:
                average["average_profit"] += v

        average["average_profit"] /= len(comp_dict)
        list_comp.append(average)

    except FileNotFoundError:
        print("You enter incorrect name file")

    return list_comp


