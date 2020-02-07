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

def option_function(option,maze):
	if option == 4:
		print('Configure current maze')
		Display_config_menu()
		config_options(maze)
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

	return "Maze Configuration Menu is displaying"

#Function for options in configuration menu - Display text and input
def config_options(maze):
	#Retrieve user input for which configuration option they want
	configOption=input("Enter your options:")
	if (0 <= int(configOption) < 5):
		configOption = int(configOption)
	else:
		print("Invalid Option!")
	#Option for creating wall
	if configOption == 1:
		print("Enter the coordinate of the item you wish to change E.g. Row, Column")
		print("'B' to return to Configure Menu.")
		inputOptions=input("'M' to return to Main Menu:")
		if inputOptions != "B" and inputOptions != "M":
			optionInput, optionInputColumn = inputOptions.split(',')
			if (optionInput.isdigit() and 0<=int(optionInput)<9 and 0<=int(optionInputColumn)<9):
				maze[int(optionInput)-1][int(optionInputColumn)-1] = "X"
				file = open('maze.csv','w')
				for row in maze:
                                	for col in row:
                                        	file.write(col+',')
                                	file.write('\n')
                        #file.close()
		elif inputOptions == "B":
			Display_config_menu()
		elif inputOptions == "M":
			display_menu()
		else:
			print("Invalid Option")
		return "Option Number 2: Create Passageway has been selected."

	#option for creating passageway
	elif configOption == 2:
		print("Enter the coordinate of the item you wish to change E.g. Row, Column")
		print("'B' to return to Configure Menu.")
		inputOptions=input("'M' to return to Main Menu:")
		if inputOptions != "B" and inputOptions != "M":
			optionInput, optionInputColumn = inputOptions.split(',')
			if (optionInput.isdigit() and 0<=int(optionInput)<9 and 0<=int(optionInputColumn)<9):
				maze[int(optionInput)-1][int(optionInputColumn)-1] = "O"
				file = open('maze.csv','w')
				for row in maze:
                                	for col in row:
                                        	file.write(col+',')
                                	file.write('\n')
                        #file.close()
		elif inputOptions == "B":
			Display_config_menu()
		elif inputOptions == "M":
			display_menu()
		else:
			print("Invalid Option")
		return "Option Number 2: Create Passageway has been selected."

	#option for creating startpoint
	elif configOption == 3:
		print("Enter the coordinate of the item you wish to change E.g. Row, Column")
		print("'B' to return to Configure Menu.")
		#optionInput, optionInputColumn=input("'M' to return to Main Menu:").split(',')
		inputOptions=input("'M' to return to Main Menu:")
		if inputOptions != "B" and inputOptions != "M":
			optionInputRow, optionInputColumn = inputOptions.split(',')
			if (optionInputRow.isdigit() and 0<=int(optionInputRow)<9 and 0<=int(optionInputColumn)<9):
				for row in maze:
					for col in row:
						if col == "A":
							colindex = row.index(col)
							rowindex = maze.index(row)
							maze[rowindex][colindex] = "X"
							break
						else:
							continue
				maze[int(optionInputRow)-1][int(optionInputColumn)-1] = "A"
				file = open('maze.csv','w')
				for row in maze:
					for col in row:
						file.write(col+',')
					file.write('\n')
                        #file.close()
			else:
				print("ok")

		elif inputOptions == "B":
			Display_config_menu()
		elif inputOptions == "M":
			display_menu()
		else:
			print("Invalid Option")
		return "Option Number 3: Create starting point has been selected."

	#option for creating endpoint
	elif configOption == 4:
		print("Enter the coordinate of the item you wish to change E.g. Row, Column")
		print("'B' to return to Configure Menu.")
		inputOptions=input("'M' to return to Main Menu:")
		#print(inputOptions)
		if inputOptions != "B" and inputOptions != "M":
			optionInputRow, optionInputColumn= inputOptions.split(',')
			if (optionInputRow.isdigit() and 0<=int(optionInputRow)<9 and 0<=int(optionInputColumn)<9):
				for row in maze:
					for col in row:
						if col == "B":
							colindex = row.index(col)
							rowindex = maze.index(row)
							maze[rowindex][colindex] = "X"
							break
						else:
							continue
				maze[int(optionInputRow)-1][int(optionInputColumn)-1] = "B"
				file = open('maze.csv','w')
				for row in maze:
					for col in row:
						file.write(col+',')
					file.write('\n')
                        #file.close()
		elif inputOptions == "B":
			Display_config_menu()
		elif inputOptions == "M":
			display_menu()
		else:
			print("Invalid Option")
		return "Option Number 4: Create ending point has been selected."

	else:
		print("STOP")



