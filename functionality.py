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