# functions for the program
config_menu= ["Create Wall", "Create Passageway", "Create Start Point", "Create End Point"]
import csv

# Display main menu
def display_menu():
	menu = ('''

	MAIN MENU

	=========

	[4] Configure current maze
	''')
	print(menu)
	return(menu)

def get_option():
	option = input("Enter your option:")
	if (0 <= int(option) < 5):
		option = int(option)
	else:
		print("Invalid Option!")
	return option

def option_function(option):
	if option == 4:
		print('Configure current maze')
		Display_config_menu()
	else:
		print("FAILURE")


# [1] Read and load maze from file
#Code from read file feature done by HuiLin
def read_file():
    print('Option [1] Read and load maze from file')
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


# [2] View maze
#Code from display maze feature done by HuiLin
def display_maze(maze):
    disp_maze = '\n'.join(str(row) for row in maze)
    print(disp_maze, end='')
    return disp_maze

# [3] Play maze game

# [4] Configure current maze
#Display configuration menu with options
def Display_config_menu():
	
	print("CONFIGURATION MENU")
	print("==================")
	optionNo=1
	for i in config_menu:
		print("[{0}] {1}".format(optionNo, i))
		optionNo+= 1
	print()
	print("[0] Exit to Main Menu")
	print()
	configOption=input("Enter your options:")
	if (0 <= int(configOption) < 5):
		configOption = int(configOption)
	else:
		print("Invalid Option!")
	return configOption


	return "Maze Configuration Menu is displaying"

#Function for options in configuration menu - Display text and input
def config_options(configOption,maze):
	#Option for creating wall
	if configOption == 1:
		print("Enter the coordinate of the item you wish to change E.g. Row, Column")
		print("'B' to return to Configure Menu.")
		optionInput, optionInputColumn=input("'M' to return to Main Menu:").split(',')
		if (optionInput.isdigit() and 0<=int(optionInput)<9 and 0<=int(optionInputColumn)<9):
                        #print(maze[int(optionInput)][int(optionInputColumn)])
			maze[int(optionInput)-1][int(optionInputColumn)-1] = "Z"
##			with open('maze.csv', mode='w') as maze_file:
##                                maze_writer = csv.writer(maze_file, delimiter=',',quoting=csv.QUOTE_MINIMAL)
			file = open('maze.csv','w')
			for row in maze:
                                for col in row:
                                        file.write(col+',')
                                file.write('\n')
                        #file.close()
##                        for row in maze:
##                                for col in row:
##                                        print("test")
##                                        file.write(col + ',')
##                                                maze_writer.writerow(col)
##                                        maze_writer.writerow('\n')
##                                file.write('\n')
##                        file.close()
		elif optionInput == "B":
			Display_config_menu()
		elif optionInput == "M":
			display_menu()
		else:
			print("Invalid Option")
		return "Option Number 1: Create Wall has been selected."

	else:
		print("STOP")



