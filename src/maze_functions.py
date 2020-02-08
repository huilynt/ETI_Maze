# functions for the program
import csv


# [1] Read and load maze from file
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
    print(disp_maze, end='\n')
    return disp_maze

# [3] Play maze game

def startgame():
    #display menu
    print("Option[3] Play Maze Game")
    print("=============================")
    maze = read_file()
    sc, ec = store_location(maze)
    display_maze(maze)
##    print(maze[sc[1]+1][sc[0]])
    print("Location of Start(A) : (Column {}, Row {}) ".format(sc[0]-1,sc[1]-1))
    print ("Location of End(B): (Column {}, Row {}) ".format(ec[0]-1,ec[1]-1))
    while True:
        i = input("Press 'W' for UP, 'A' for LEFT, 'S' for Down, 'D' for RIGHT, 'M' for Main Menu:")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        maze,sc = move(i,sc,ec,maze)
        display_maze(maze)

=======
        maze = move(i,sc,ec,maze)
        
>>>>>>> parent of ff2135c... finished basic gameplay
=======
        maze = move(i,sc,ec,maze)
        
>>>>>>> parent of ff2135c... finished basic gameplay
=======
        maze = move(i,sc,ec,maze)
        
>>>>>>> parent of ff2135c... finished basic gameplay

def move(i,sc,ec,maze):
    #if user enter "W"
    acoor = {"x":sc[0], "y":sc[1]}
    if ( i == "w"):
        newsc = [acoor["x"],acoor["y"]-1]
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> parent of ff2135c... finished basic gameplay
=======
>>>>>>> parent of ff2135c... finished basic gameplay
=======
>>>>>>> parent of ff2135c... finished basic gameplay
=======
        print(newsc)
>>>>>>> parent of 3e3b6b3... completed features, working on unit test
        #check if move is valid ( maze[y,x] to navigate through maze
        if(maze[newsc[1]][newsc[0]] == "O"):
                #set current position to O
                maze[acoor.y,acoor.x] = "O"
                #set new position to A
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                maze[newsc[1]][newsc[0]] = "A"
                return maze, newsc
        else:
            print("Invalid Move, Try Again")
            
    elif (i== "s"):
        newsc = [acoor["x"],acoor["y"]+1]
        print(newsc)
        #check if move is valid ( maze[y,x] to navigate through maze
        if(maze[newsc[1]][newsc[0]] == "O"):
                #set current position to O
                maze[acoor["y"]][acoor["x"]] = "O"
                #set new position to A
                maze[newsc[1]][newsc[0]] = "A"
                return maze, newsc
        else:
            print("Invalid Move, Try Again")
            
    elif (i== "a"):
        newsc = [acoor["x"]-1,acoor["y"]]
        print(newsc)
        #check if move is valid ( maze[y,x] to navigate through maze
        if(maze[newsc[1]][newsc[0]] == "O"):
                #set current position to O
                maze[acoor["y"]][acoor["x"]] = "O"
                #set new position to A
                maze[newsc[1]][newsc[0]] = "A"
                return maze, newsc
##                return mazeleft
        else:
            print("Invalid Move, Try Again")
            
    elif (i== "d"):
        newsc = [acoor["x"]+1,acoor["y"]]
        print(newsc)
        #check if move is valid ( maze[y,x] to navigate through maze
        if(maze[newsc[1]][newsc[0]] == "O"):
                #set current position to O
                maze[acoor["y"]][acoor["x"]] = "O"
                #set new position to A
                maze[newsc[1]][newsc[0]] = "A"
                return maze, newsc
                print(maze)
        else:
            print("Invalid Move, Try Again")
    return maze, newsc
=======
=======
>>>>>>> parent of ff2135c... finished basic gameplay
=======
>>>>>>> parent of ff2135c... finished basic gameplay
                maze[newsc[1]][newsc[0]] == "A"
                return mazeup
        else:
                print("Invalid Move, Try Again")
    return maze
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of ff2135c... finished basic gameplay

<<<<<<< HEAD
=======
>>>>>>> parent of ff2135c... finished basic gameplay
=======
>>>>>>> parent of ff2135c... finished basic gameplay

=======
>>>>>>> parent of 3e3b6b3... completed features, working on unit test
# [4] Configure current maze
