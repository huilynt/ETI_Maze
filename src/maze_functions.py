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

# [3] Play maze game

def startgame():
    #display menu
    print("Option[3] Play Maze Game")
    print("=============================")
    maze = read_file()
    sc, ec = store_location(maze)
    sc[0]-=1
    sc[1]-=1
    display_maze(maze)
##    print(maze[sc[1]+1][sc[0]])
    print("Location of Start(A) : (Column {}, Row {}) ".format(sc[0],sc[1]))
    print ("Location of End(B): (Column {}, Row {}) ".format(ec[0],ec[1]-1))
    while True:
        i = input("Press 'W' for UP, 'A' for LEFT, 'S' for Down, 'D' for RIGHT, 'M' for Main Menu:")
        maze,sc = move(i,sc,ec,maze)
##        display_maze(maze)


def move(i,sc,ec,maze):
    #if user enter "W"
    acoor = {"x":sc[0], "y":sc[1]}
    if ( i == "w"):
        newsc = [acoor["x"],acoor["y"]-1]

        #check if move is valid ( maze[y,x] to navigate through maze
        if(maze[newsc[1]][newsc[0]] == "O"):
                #set current position to O
                maze[acoor["y"]][acoor["x"]] = "O"
                #set new position to A
                maze[newsc[1]][newsc[0]] = "A"
                display_maze(maze)
                return maze, newsc
        elif(maze[newsc[1]][newsc[0]] == "X"):
                print("Invalid Move, Try Again")
                maze[acoor["y"]][acoor["x"]] = "A"
                maze[newsc[1]][newsc[0]] = "X"
                newsc = [acoor["x"],acoor["y"]]
                display_maze(maze)
                return maze, newsc
        elif(maze[newsc[1]][newsc[0]] == "B"):
            print("Game Completed")
            return maze, newsc
                
            
    elif (i== "s"):
        newsc = [acoor["x"],acoor["y"]+1]

        #check if move is valid ( maze[y,x] to navigate through maze
        if(maze[newsc[1]][newsc[0]] == "O"):
                 #set current position to O
                maze[acoor["y"]][acoor["x"]] = "O"
                #set new position to A
                maze[newsc[1]][newsc[0]] = "A"
                display_maze(maze)
                return maze, newsc
            
        elif(maze[newsc[1]][newsc[0]] == "X"):
                print("Invalid Move, Try Again")
                maze[acoor["y"]][acoor["x"]] = "A"
                maze[newsc[1]][newsc[0]] = "X"
                newsc = [acoor["x"],acoor["y"]]
                display_maze(maze)
                return maze, newsc
        elif(maze[newsc[1]][newsc[0]] == "B"):
            print("Game Completed")
            return maze, newsc
                
            
    elif (i== "a"):
        newsc = [acoor["x"]-1,acoor["y"]]
 
        #check if move is valid ( maze[y,x] to navigate through maze
        if(maze[newsc[1]][newsc[0]] == "O"):
                #set current position to O
                maze[acoor["y"]][acoor["x"]] = "O"
                #set new position to A
                maze[newsc[1]][newsc[0]] = "A"
                display_maze(maze)
                return maze, newsc
##                return mazeleft
            
        elif(maze[newsc[1]][newsc[0]] == "X"):
                print("Invalid Move, Try Again")
                maze[acoor["y"]][acoor["x"]] = "A"
                maze[newsc[1]][newsc[0]] = "X"
                newsc = [acoor["x"],acoor["y"]]
                display_maze(maze)
                return maze, newsc
        elif(maze[newsc[1]][newsc[0]] == "B"):
            print("Game Completed")
            return maze, newsc

            
    elif (i== "d"):
        newsc = [acoor["x"]+1,acoor["y"]]
        #check if move is valid ( maze[y,x] to navigate through maze
        if(maze[newsc[1]][newsc[0]] == "O"):
                #set current position to O
                maze[acoor["y"]][acoor["x"]] = "O"
                #set new position to A
                maze[newsc[1]][newsc[0]] = "A"
                display_maze(maze)
                return maze, newsc

        elif(maze[newsc[1]][newsc[0]] == "X"):
                print("Invalid Move, Try Again")
                maze[acoor["y"]][acoor["x"]] = "A"
                maze[newsc[1]][newsc[0]] = "X"
                newsc = [acoor["x"],acoor["y"]]
                display_maze(maze)
                return maze, newsc
        elif(maze[newsc[1]][newsc[0]] == "B"):
            print("Game Completed")
            return maze, newsc

    elif (i== "m"):
        newsc = [acoor["x"],acoor["y"]]
        display_menu()
        return maze, newsc

    elif (i!= "w","a","s","d","m"):
        newsc = [acoor["x"],acoor["y"]]
        print("Please enter a valid letter!")
        display_maze(maze)
        return maze, newsc
         
    return maze, newsc


# [4] Configure current maze
