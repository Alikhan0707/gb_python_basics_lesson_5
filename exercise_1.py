from func_to_easy import write_data_to_file
from os import path

while True:

    user_data = input("Enter any data that you want! To quit enter 'q': ")
    file_name = "data_from_user.txt"

    if user_data.lower() == 'q':

        break

    elif path.exists(file_name):

        write_data_to_file(file_name, user_data, indent=True)

    else:

        write_data_to_file(file_name, user_data, new=True, indent=True)