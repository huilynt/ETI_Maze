# functions for the program
config_menu= ["Create Wall", "Create Passageway", "Create Start Point", "Create End Point"]

# Display main menu

# [1] Read and load maze from file

# [2] View maze

# [3] Play maze game

# [4] Configure current maze
def configure_maze_menu():
	print("CONFIGURATION MENU")
	print("==================")
	optionNo=1
	for i in config_menu:
		print("[{0}] {1}".format(optionNo, i))
		optionNo+= 1
	print()
	print("[0] Exit to Main Menu")
	return "Maze Configuration Menu is displaying"