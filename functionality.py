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


def count_lines_and_simbols(name):

    list_line_len = []

    try:
        with open(name) as f:

            for line in f:

                list_line_len.append(len(line))

    except IOError:
        print("Some error")
    return list_line_len


def workers_data(name):

    """

    :param name: file name
    :return: workers dictionary
    """

    workers_dict = {}

    try:

        with open(name) as f:

            for line in f:

                split_line = line.split(":")
                workers_dict[split_line[0]] = split_line[1]

    except IOError:
        print("Some error")

    return workers_dict