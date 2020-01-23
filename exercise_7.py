from func_to_easy import read_line_by_line, split_string, sum_number_in_list, write_data_to_file

file_name = "firm_data.txt"

json_file = "firm_data.json"

firm_list = []

firm_dict = {}

average = {"average_profit": 0}

data = read_line_by_line(file_name)

for i in data:

    splitted = split_string(i)

    profit = sum_number_in_list(splitted)

    firm_dict[splitted[0]] = profit

    if profit > 0:

        average["average_profit"] += profit

firm_list.append(firm_dict)
firm_list.append(average)

