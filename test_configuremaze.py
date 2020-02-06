import pytest
import unittest
from unittest import mock
from unittest import TestCase
from unittest.mock import patch
from src.maze_functions import *

#Test for displaying configuration menu

def test_display_config_menu():
	working = Display_config_menu()
	assert working == "Maze Configuration Menu is displaying"

#Test for creating wall
@patch('builtins.input')
def test_create_wall(mocked_input):
	mocked_input.side_effect = ["maze.csv", "4", "1", "6,2"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert maze[6][2] == "X"

#Test for creating passageway
@patch('builtins.input')
def test_create_passageway(mocked_input):
	mocked_input.side_effect = ["maze.csv", "4", "2", "2,5"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert maze[2][5] == "O"

#Test for creating startpoint
@patch('builtins.input')
def test_create_startpoint(mocked_input):
	mocked_input.side_effect = ["maze.csv", "4", "3", "1,6"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert maze[1][6] == "A"

#Test for creating endpoint
def test_create_endpoint():
	mocked_input.side_effect = ["maze.csv", "4", "4", "7,1"]
	maze = read_file()
	display_menu()
	option= get_option()
	option_function(option,maze)
	assert maze[7][1] == "B"

#Test for exiting to main menu from configuration
def test_exit_mainmenu():
	choice= configChoice("B")
	assert value == True

#Test for exiting to configuration menu
def test_exit_configmenu():
	choice= configChoice("M")
	assert value == True
