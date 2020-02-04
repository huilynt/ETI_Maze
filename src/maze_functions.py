# functions for the program

import csv


# Display main menu
# Display main menu and return it
def display_menu():
    menu = ('''
    MAIN MENU
    =========
    [1] Read and load maze from file
    [2] View maze
    [3] Play maze game
    [4] Configure current maze

    [0] Exit maze
    ''')
    print(menu)
    return menu


# Get user input for option
# validate (option is in 0 to 4 range) and return it as int
# else return -1 as invalid indicator
def get_option():
    option = input('Enter your option: ')
    if (option.isdigit() and 0 <= int(option) < 5):
        option = int(option)
    else:
        option = -1
    return option


# # Given a valid option (from get_option())
# # print the option title
# # run the corresponding function for each option
# # breaks the program by returning a False when option is 0
# # else always return True to keep main program running
# # def option_functions(option):
#     maze = []
#     return_var = True
#     if option == 1:
#         print('Read and load maze from file')
#         maze = read_file()
#     elif option == 2:
#         print('View maze')

#     elif option == 3:
#         print('Play maze game')
#     elif option == 4:
#         print('Configure current maze')
#     elif option == 0:
#         print('Exit maze')
#         return_var = False
#     else:
#         print('Invalid option! Please try again!')

#     return return_var, maze


# [1] Read and load maze from file
def read_file():
    file_name = input('Enter the name of the data file: ')
    maze = []
    num_lines = 0
    if '.csv' in file_name:
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                maze.append(row)
            num_lines = csv_reader.line_num
        print('Number of lines read: {}'.format(num_lines))
    else:
        print('Invalid file type!')
        return -1
    return maze


def store_location(maze):
    start_coordinate = []
    end_coordinate = []
    for row_index, row in enumerate(maze):
        for column_index, column in enumerate(row):
            if (column == 'A'):
                start_coordinate.append(column_index + 1)
                start_coordinate.append(row_index + 1)
                break
            elif (column == 'B'):
                end_coordinate.append(column_index + 1)
                end_coordinate.append(row_index + 1)
                break
    if (len(start_coordinate) == 0 or len(end_coordinate) == 0):
        print('Invalid maze!')
        return -1, -1

    return start_coordinate, end_coordinate


# [2] View maze
def display_maze(maze):
    disp_maze = '\n'.join(str(row) for row in maze)
    print(disp_maze)
    return disp_maze


# [3] Play maze game

# [4] Configure current maze
