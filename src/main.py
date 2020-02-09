from maze_functions import *

# Main program structure
# running keeps the program alive, break my option_functions returning False
# more info in option_functions() in maze_functions.py
running = True
maze = []
start = []
end = []
while running:
    display_menu()
    option = get_option()
    if option == 1:
        print('[1] Read and load maze from file')
        maze = read_file()
        start, end = store_location(maze)
    elif option == 2:
        print('[2] View maze')
        display_maze(maze)
    elif option == 3:
        print('[3] Play maze game')
    elif option == 4:
        print('[4] Configure current maze')
        print("")
        display_maze(maze)
        print("")
        option_function(option,maze)
    elif option == 0:
        print('[0] Exit maze')
        running = False
    else:
        print('Invalid option! Please try again!')
