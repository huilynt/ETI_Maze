import csv

# Display main menu


# [1] Read and load maze from file
def read_file():
    print('Option [1] Read and load maze from file')
    file_name = input('Enter the name of the data file: ')
    maze = []
    num_lines = 0
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            maze.append(row)
        num_lines = csv_reader.line_num
    print('Number of lines read: {}'.format(num_lines))
    return maze


def store_location(maze):
    start_coordinate = []
    end_coordinate = []
    for row_index, row in enumerate(maze):
        print(row)
        for column_index, column in enumerate(row):
            if (column == 'A'):
                start_coordinate.append(column_index + 1)
                start_coordinate.append(row_index + 1)
                break
            elif (column == 'B'):
                end_coordinate.append(column_index + 1)
                end_coordinate.append(row_index + 1)
                break
    # location = [start_coordinate, end_coordinate]
    return start_coordinate, end_coordinate


# [2] View maze
def display_maze(maze):
    disp_maze = '\n'.join(str(row) for row in maze)
    print(disp_maze, end='')
    return disp_maze


# [3] Play maze game

# [4] Configure current maze

# Main program
# maze = read_file()
# print(maze)
# maze = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
#         ['X', 'O', 'O', 'O', 'X', 'O', 'A', 'X'],
#         ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'],
#         ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
#         ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
#         ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
#         ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'],
#         ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']]
# display_maze(maze)