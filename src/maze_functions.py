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


# Given a valid option (from get_option())
# print the option title
# run the corresponding function for each option
# breaks the program by returning a False when option is 0
# else always return True to keep main program running
def option_functions(option):
    return_var = True
    if option == 1:
        print('Read and load maze from file')
    elif option == 2:
        print('View maze')
    elif option == 3:
        print('Play maze game')
    elif option == 4:
        print('Configure current maze')
    elif option == 0:
        print('Exit maze')
        return_var = False
    else:
        print('Invalid option! Please try again!')

    return return_var


# [1] Read and load maze from file

# [2] View maze

# [3] Play maze game

# [4] Configure current maze