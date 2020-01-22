from func_to_easy import split_string, translate, read_line_by_line, write_data_to_file
from os import path

translator = {"one": "один", "two": "два", "three": "три", "four": "четыре"}

file_name = "some_text.txt"

new_file_name = "new_text.txt"

list_lines = read_line_by_line(file_name)

for line in list_lines:

    splitted = split_string(line)

    trans_list = translate(translator, splitted)

    translated_data = f"{trans_list[0].title()} {trans_list[1]} {trans_list[2]}"

    if path.exists(file_name):

        write_data_to_file(new_file_name, translated_data, indent=True)

    else:

        write_data_to_file(new_file_name, translated_data, new=True, indent=True)