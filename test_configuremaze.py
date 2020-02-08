import pytest
import unittest
from unittest import mock
from unittest import TestCase
from unittest.mock import patch
from src.maze_functions import *

#Test for displaying configuration menu (PASSING)

def test_display_config_menu():
	working = Display_config_menu()
	assert working == "Maze Configuration Menu is displaying"

#Test for creating wall (PASSING)
@patch('builtins.input')
def test_create_wall(mocked_input):
	mocked_input.side_effect = ["maze.csv", "4", "1", "6,2"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert maze[5][1] == "X"

#Test for creating passageway (PASSING)
@patch('builtins.input')
def test_create_passageway(mocked_input):
	mocked_input.side_effect = ["maze.csv", "4", "2", "2,5"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert maze[1][4] == "O"

#Test for creating startpoint (PASSING)
@patch('builtins.input')
def test_create_startpoint(mocked_input):
	mocked_input.side_effect = ["maze.csv", "4", "3", "1,6"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert maze[0][5] == "A"

#Test for creating endpoint (PASSING)
@patch('builtins.input')
def test_create_endpoint(mocked_input):
	mocked_input.side_effect = ["maze.csv", "4", "4", "7,1"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert maze[6][0] == "B"

#Test for exiting to main menu from configuration (PASSING)
@patch('builtins.input')
def test_exit_mainmenu(mocked_input):
	mocked_input.side_effect = ["maze.csv", "4", "1", "M"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert '''
    MAIN MENU
    =========
    [1] Read and load maze from file
    [2] View maze
    [3] Play maze game
    [4] Configure current maze

    [0] Exit maze
    ''' == display_menu()

#Test for exiting to configuration menu (PASSING)
@patch('builtins.input')
def test_exit_configmenu(mocked_input):
	mocked_input.side_effect = ["maze.csv", "4", "1", "B"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert "Maze Configuration Menu is displaying" == Display_config_menu()

#Test for invalid input on create wall option (FAILING)
@pytest.mark.xfail
@patch('builtins.input')
def test_create_wall_failing(mocked_input):
	mocked_input.side_effect = ["maze.csv", "4", "#", "6,2"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert maze[5][1] == "X"

#Test for invalid input on main menu option (FAILING)
@pytest.mark.xfail
@patch('builtins.input')
def test_create_passageway_failing(mocked_input):
	mocked_input.side_effect = ["maze.csv", "#", "2", "2,5"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert maze[1][4] == "O"

#Test for invalid input on loading maze file (FAILING)
@pytest.mark.xfail
@patch('builtins.input')
def test_load_maze_failing(mocked_input):
	mocked_input.side_effect = ["mazeMAZE.csv", "4", "2", "2,5"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert maze[1][4] == "O"