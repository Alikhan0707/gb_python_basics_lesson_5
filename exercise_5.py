from func_to_easy import write_data_to_file, sum_number_in_list, read_line_by_line, split_string
from os import path

num_list = [i for i in range(15, 300) if i % 5 == 0]

file_name = "numbers.txt"

sum_numbers = 0

for i in num_list:
    if path.exists(file_name):

        write_data_to_file(file_name, f"{i} ")

    else:

        write_data_to_file(file_name, f"{i} ", new=True)


data = read_line_by_line(file_name)

for i in data:

    splitted = split_string(i)

    sum_of = sum_number_in_list(splitted)

    sum_numbers += sum_of

print(sum_numbers)