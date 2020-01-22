from func_to_easy import read_line_by_line, split_string, sum_number_in_list

lessons_dict = {}

file_name = "lesson.txt"

data = read_line_by_line(file_name)

for i in data:
    splitted = split_string(i)

    count_lessons = sum_number_in_list(splitted)

    lessons_dict[splitted[0].title()] = count_lessons

print(lessons_dict)