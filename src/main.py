# program will run here
from maze_functions import *
import csv

while True:
    maze=read_file()
    display_maze(maze)
    display_menu()
    option= get_option()
    option_function(option,maze)



