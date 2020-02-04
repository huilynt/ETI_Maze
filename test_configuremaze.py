import pytest
import unittest
from src.maze_functions import *

#Test for displaying configuration menu

def test_display_config_menu():
	working = Display_config_menu()
	assert working == "Maze Configuration Menu is displaying"

#Test for creating wall
def test_create_wall():
	option=4
	option_function(option)
	maze=read_file()
	configOption=1
	config_options(configOption)
	assert maze_functions.maze[2][1] == "X"

#Test for creating passageway
def test_create_passageway():
	createPassageway(3,1)
	assert maze[3][1] == "O"

#Test for creating startpoint
def test_create_startpoint():
	createStartpoint(5,1)
	assert maze[5][1] == "A"

#Test for creating endpoint
def test_create_endpoint():
	createEndpoint(1,8)
	assert maze[1][8] == "B"

#Test for exiting to main menu from configuration
def test_exit_mainmenu():
	choice= configChoice("B")
	assert value == True

#Test for exiting to configuration menu
def test_exit_configmenu():
	choice= configChoice("M")
	assert value == True
