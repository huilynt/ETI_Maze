from maze_functions import *

# Main program structure
# running keeps the program alive, break my option_functions returning False
# more info in option_functions() in maze_functions.py
running = True
while running:
    display_menu()
    option = get_option()
    running = option_functions(option)
