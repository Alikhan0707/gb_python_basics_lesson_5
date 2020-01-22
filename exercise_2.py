from func_to_easy import read_line_by_line, split_string


file_name = "new_text.txt"

lines = read_line_by_line(file_name)

count_of_lines = len(lines)

print(f"Общее количество строк: {count_of_lines}")

for i in lines:

    stripped = i.strip()
    split_line = split_string(stripped)

    print(f"Количество слов в строке: {len(split_line)}")