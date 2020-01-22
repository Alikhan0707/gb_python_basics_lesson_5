from func_to_easy import read_line_by_line

file_name = "worker_data.txt"

data = read_line_by_line(file_name)

small_payment_workers = {}

data_list = []


for i in data:

    splitted = i.split()

    data_list.append(float(splitted[1]))

    if float(splitted[1]) < 20000:

        small_payment_workers[splitted[0]] = splitted[1]

for k, v in small_payment_workers.items():

    print(f"This workers have less than 20000 payment for month: {k.title()} - {v}")

average = sum(data_list) / len(data)

print(round(average, 2))