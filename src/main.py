# Display main menu
def display_menu():
    menu = '''
    MAIN MENU
    =========
    [1] Read and load maze from file
    [2] View maze
    [3] Play maze game
    [4] Configure current maze

    [0] Exit maze
    '''
    print(menu)
    return menu


def get_option():
    option = input('Enter your option: ')
    if option.isdigit():
        option = int(option)
    else:
        option = -1
        print('Invalid option!')
    return option


def option_functions(option):
    message = ''
    if option == 1:
        message = 'Read and load maze from file'
    elif option == 2:
        message = 'View maze'
    elif option == 3:
        message = 'Play maze game'
    elif option == 4:
        message = 'Configure current maze'
    elif option == 0:
        message = 'Exit maze'
    else:
        message = 'Invalid option!'
    print(message)
    return message


# [1] Read and load maze from file

# [2] View maze

# [3] Play maze game

# [4] Configure current maze

# while True:
#     display_menu()
#     option = get_option()